import yfinance as yf
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pytz

# Initialize the Dash app
app = dash.Dash(__name__)

# Get Remedy stock data
stock = yf.Ticker("REMEDY.HE")
df = stock.history(period="2y")  # Get 2 years of data

# Create the app layout
app.layout = html.Div([
    html.H1('Remedy Entertainment Stock Analysis', 
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginTop': '20px'}),
    
    # Time range selector
    dcc.RadioItems(
        id='timeframe',
        options=[
            {'label': '1M', 'value': 30},
            {'label': '3M', 'value': 90},
            {'label': '6M', 'value': 180},
            {'label': '2Y', 'value': 730},
            {'label': '1Y', 'value': 365},
        ],
        value=180,
        inline=True,
        style={'textAlign': 'center', 'marginBottom': '20px'}
    ),
    
    # Candlestick chart
    dcc.Graph(id='stock-graph')
])

# Callback to update the graph based on timeframe selection
@app.callback(
    Output('stock-graph', 'figure'),
    Input('timeframe', 'value')
)
def update_graph(selected_days):
    filtered_df = df.copy()
    
    if selected_days == 'ytd':
        start_date = datetime(datetime.now().year, 1, 1)
        filtered_df = df[df.index >= start_date]
    else:
        # Filter last N days
        filtered_df = df.iloc[-selected_days:]
    
    # Create the candlestick chart
    fig = go.Figure(data=[go.Candlestick(x=filtered_df.index,
                                        open=filtered_df['Open'],
                                        high=filtered_df['High'],
                                        low=filtered_df['Low'],
                                        close=filtered_df['Close'],
                                        name='REMEDY')])
    
    # Add volume bars
    fig.add_trace(go.Bar(x=filtered_df.index, 
                        y=filtered_df['Volume'],
                        name='Volume',
                        yaxis='y2',
                        marker_color='rgba(128,128,128,0.5)'))
    
    # Update layout
    fig.update_layout(
        title='Remedy Entertainment (REMEDY.HE)',
        yaxis_title='Stock Price (EUR)',
        yaxis2=dict(
            title='Volume',
            overlaying='y',
            side='right'
        ),
        xaxis_rangeslider_visible=False,
        template='plotly_white',
        height=800
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)