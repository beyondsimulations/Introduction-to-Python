from nicegui import ui
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta
import asyncio
from plotly.subplots import make_subplots

STOCK_SYMBOL = "REMEDY.HE"
TIME_PERIODS = {
    '1D': '1d',
    '5D': '5d',
    '1M': '1mo',
    '3M': '3mo',
    '6M': '6mo',
    '1Y': '1y',
    '2Y': '2y'
}

class StockDashboard:
    def __init__(self):
        self.current_period = '1D'
        self.intervals = {
            '1D': '1m',
            '5D': '5m',
            '1M': '1h',
            '3M': '1d',
            '6M': '1d',
            '1Y': '1d',
            '2Y': '1d'
        }

    async def update_stock_data(self):
        while True:
            await self.fetch_and_display_data()
            # Update more frequently for intraday data, less for historical
            await asyncio.sleep(60 if self.current_period == '1D' else 300)

    async def fetch_and_display_data(self):
        stock = yf.Ticker(STOCK_SYMBOL)
        period = TIME_PERIODS[self.current_period]
        interval = self.intervals[self.current_period]
        
        hist = stock.history(period=period, interval=interval)
        
        if not hist.empty:
            current_price = hist['Close'].iloc[-1]
            prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else hist['Close'].iloc[0]
            price_change = current_price - prev_close
            price_change_pct = (price_change / prev_close) * 100
            
            # Update price displays
            self.price_display.set_text(f"€{current_price:.2f}")
            self.change_display.set_text(
                f"{'▲' if price_change >= 0 else '▼'} €{abs(price_change):.2f} ({price_change_pct:.2f}%)"
            )
            self.change_display.classes(
                remove='text-red-500 text-green-500',
                add='text-green-500' if price_change >= 0 else 'text-red-500'
            )

            # Create subplot with stock price and volume
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                              vertical_spacing=0.03, 
                              row_heights=[0.7, 0.3])

            # Add candlestick
            fig.add_trace(go.Candlestick(
                x=hist.index,
                open=hist['Open'],
                high=hist['High'],
                low=hist['Low'],
                close=hist['Close'],
                name='Price'
            ), row=1, col=1)

            # Add volume bars
            colors = ['red' if row['Open'] > row['Close'] else 'green' 
                     for index, row in hist.iterrows()]
            fig.add_trace(go.Bar(
                x=hist.index,
                y=hist['Volume'],
                name='Volume',
                marker_color=colors
            ), row=2, col=1)

            # Update layout
            fig.update_layout(
                title=f'Remedy Entertainment ({STOCK_SYMBOL}) - {self.current_period}',
                yaxis_title='Price (EUR)',
                yaxis2_title='Volume',
                xaxis_rangeslider_visible=False,
                template='plotly_dark',
                height=800
            )

            self.chart.update_figure(fig)

    def period_selector(self, period: str):
        self.current_period = period
        asyncio.create_task(self.fetch_and_display_data())

@ui.page('/')
def dashboard():
    ui.dark_mode().enable()
    
    stock_dash = StockDashboard()
    
    with ui.column().classes('w-full max-w-7xl mx-auto p-4'):
        ui.label('Remedy Entertainment Stock Dashboard').classes('text-h3 text-center mb-4')
        
        # Price and change display
        with ui.row().classes('w-full justify-center items-center gap-4'):
            stock_dash.price_display = ui.label('Loading...').classes('text-h4')
            stock_dash.change_display = ui.label('').classes('text-h5')

        # Time period selector
        with ui.row().classes('w-full justify-center gap-2 my-4'):
            for period in TIME_PERIODS.keys():
                ui.button(period, 
                         on_click=lambda p=period: stock_dash.period_selector(p)
                         ).classes('px-4 py-2')

        # Chart
        stock_dash.chart = ui.plotly({}).classes('w-full')
        
        # Additional info
        with ui.row().classes('w-full justify-center gap-4 mt-4'):
            ui.button('Refresh', 
                     on_click=lambda: asyncio.create_task(stock_dash.fetch_and_display_data())
                     ).classes('px-6')

    asyncio.create_task(stock_dash.update_stock_data())

ui.run(title='Remedy Stock Dashboard', port=8080)