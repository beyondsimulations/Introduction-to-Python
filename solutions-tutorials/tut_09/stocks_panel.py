import panel as pn
import yfinance as yf
from bokeh.plotting import figure
from bokeh.models import HoverTool, CrosshairTool
from datetime import datetime
import pandas as pd

# Enable Panel extensions
pn.extension(sizing_mode="stretch_width")

# Cache function for data loading
@pn.cache(ttl=3600)
def load_data(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)
        df = stock.history(period="2y")
        if df.empty:
            raise ValueError("No data available for this ticker")
        return df, None
    except Exception as e:
        return None, str(e)

def create_candlestick_plot(df, ticker_symbol):
    # Create Bokeh figure
    p = figure(
        width=800,
        height=400,
        title=f'{ticker_symbol} Stock Price',
        x_axis_type='datetime',
        tools='pan,wheel_zoom,box_zoom,reset,save'
    )
    
    # Add hover tool with formatters
    hover = HoverTool(
        tooltips=[
            ('Date', '@x{%F}'),
            ('Open', '$@{Open}{0,0.00}'),
            ('High', '$@{High}{0,0.00}'),
            ('Low', '$@{Low}{0,0.00}'),
            ('Close', '$@{Close}{0,0.00}')
        ],
        formatters={"@x": "datetime"}
    )
    
    # Add tools
    p.add_tools(hover)
    p.add_tools(CrosshairTool())
    p.add_tools(CrosshairTool())
    
    # Calculate candlestick colors
    inc = df.Close > df.Open
    dec = df.Open > df.Close
    
    # Add candlestick chart
    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.vbar(
        x=df.index[inc],
        top=df.Open[inc],
        bottom=df.Close[inc],
        width=24*60*60*1000,  # One day in milliseconds
        fill_color="green",
        line_color="green"
    )
    p.vbar(
        x=df.index[dec],
        top=df.Open[dec],
        bottom=df.Close[dec],
        width=24*60*60*1000,
        fill_color="red",
        line_color="red"
    )
    
    return p

def create_volume_plot(df):
    # Create volume subplot
    v = figure(
        width=800,
        height=200,
        x_axis_type='datetime',
        title='Volume'
    )
    
    v.vbar(
        x=df.index,
        top=df.Volume,
        width=24*60*60*1000,
        color='gray',
        alpha=0.5
    )
    
    return v

# Create error text widget with visibility control
error_text = pn.widgets.StaticText(name='Error', styles={'color': 'red'}, visible=False)

def update_plots(event):
    # Show loading indicator
    loading.visible = True
    error_text.visible = False  # Hide error message at start
    error_text.value = ""
    
    try:
        # Validate ticker symbol
        if not ticker.value or len(ticker.value) < 1:
            raise ValueError("Please enter a valid ticker symbol")
            
        # Get data
        df, error = load_data(ticker.value)
        if error:
            raise ValueError(error)
            
        days = int(timeframe.value[1])
        filtered_df = df.iloc[-days:]
        
        # Update plots
        main_plot.object = create_candlestick_plot(filtered_df, ticker.value)
        volume_plot.object = create_volume_plot(filtered_df)
        
        # Update metrics with better formatting using iloc
        latest_close = filtered_df['Close'].iloc[-1]
        prev_close = filtered_df['Close'].iloc[-2]
        daily_change_val = ((latest_close - prev_close) / prev_close * 100)
        
        current_price.value = f"${latest_close:.2f}"
        daily_change.value = f"{daily_change_val:+.2f}%"  # Added plus sign for positive values
        highest_price.value = f"${filtered_df['High'].max():.2f}"
        lowest_price.value = f"${filtered_df['Low'].min():.2f}"
        
        # Style daily change based on value
        daily_change.styles = {'color': 'green' if daily_change_val > 0 else 'red'}
        
    except Exception as e:
        error_text.value = str(e)
        error_text.visible = True  # Only show when there's an error
        error_text.styles = {'color': 'red'}
    finally:
        loading.visible = False

# Create widgets
ticker = pn.widgets.TextInput(
    name='Stock Ticker', 
    value='REMEDY.HE',
)
timeframe = pn.widgets.Select(
    name='Timeframe',
    options=[
        ('1 Month', 30),
        ('3 Months', 90),
        ('6 Months', 180),
        ('1 Year', 365),
        ('2 Years', 730)
    ],
    value=('1 Month', 30)
)

# Create additional widgets
loading = pn.indicators.LoadingSpinner(value=True, size=25)

# Update metrics styling
current_price = pn.widgets.StaticText(name='Current Price', styles={'font-weight': 'bold'})
daily_change = pn.widgets.StaticText(name='Daily Change', styles={'font-weight': 'bold'})
highest_price = pn.widgets.StaticText(name='Highest Price')
lowest_price = pn.widgets.StaticText(name='Lowest Price')
error_text = pn.widgets.StaticText(name='Error', styles={'color': 'red'})

# Update layout with loading indicator
metrics = pn.Row(
    pn.Column(current_price, daily_change),
    pn.Column(highest_price, lowest_price),
    loading
)

# Create plot panes (initially empty)
main_plot = pn.pane.Bokeh()
volume_plot = pn.pane.Bokeh()

# Watch for changes
ticker.param.watch(update_plots, 'value')
timeframe.param.watch(update_plots, 'value')

# Layout
sidebar = pn.Column(
    pn.pane.Markdown('# Settings'),
    ticker,
    timeframe,
    width=300
)

metrics = pn.Row(
    pn.Column(current_price, daily_change),
    pn.Column(highest_price),
    pn.Column(lowest_price)
)

main_content = pn.Column(
    pn.pane.Markdown('# Stock Price Analysis'),
    main_plot,
    volume_plot,
    metrics,
    error_text,  # It will only be visible when there's an error
    pn.pane.Markdown('---\nData provided by Yahoo Finance')
)

# Create template
template = pn.template.FastListTemplate(
    title='Stock Analyzer',
    sidebar=[sidebar],
    main=[main_content],
)

# Initial update
update_plots(None)

# Serve the dashboard
template.servable()