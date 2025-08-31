import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Analyzer", layout="wide")

# Title
st.title('Stock Price Analysis')

# Sidebar controls
with st.sidebar:
    st.header('Settings')

    # Stock ticker input
    ticker = st.text_input('Stock Ticker', 'REMEDY.HE')

    # Time range selector
    timeframe = st.radio(
        'Select Timeframe',
        options=[
            ('1 Month', 30),
            ('3 Months', 90),
            ('6 Months', 180),
            ('1 Year', 365),
            ('2 Years', 730)
        ],
        format_func=lambda x: x[0]
    )

# Fetch data
@st.cache_data(ttl=3600)  # Cache data for 1 hour
def load_data(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    return stock.history(period="2y")

try:
    # Load the data
    df = load_data(ticker)

    # Filter based on selected timeframe
    filtered_df = df.iloc[-timeframe[1]:]

    # Create candlestick chart
    fig = go.Figure()

    # Add candlestick
    fig.add_trace(go.Candlestick(
        x=filtered_df.index,
        open=filtered_df['Open'],
        high=filtered_df['High'],
        low=filtered_df['Low'],
        close=filtered_df['Close'],
        name='OHLC'
    ))

    # Add volume bars
    fig.add_trace(go.Bar(
        x=filtered_df.index,
        y=filtered_df['Volume'],
        name='Volume',
        yaxis='y2',
        marker_color='rgba(128,128,128,0.5)'
    ))

    # Update layout
    fig.update_layout(
        title=f'{ticker} Stock Price',
        yaxis_title='Stock Price',
        yaxis2=dict(
            title='Volume',
            overlaying='y',
            side='right'
        ),
        xaxis_rangeslider_visible=False,
        template='plotly_white',
        height=600
    )

    # Display the chart
    st.plotly_chart(fig, use_container_width=True)

    # Display additional information
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Current Price",
            f"${filtered_df['Close'][-1]:.2f}",
            f"{((filtered_df['Close'][-1] - filtered_df['Close'][-2]) / filtered_df['Close'][-2] * 100):.2f}%"
        )

    with col2:
        st.metric(
            "Highest Price",
            f"${filtered_df['High'].max():.2f}"
        )

    with col3:
        st.metric(
            "Lowest Price",
            f"${filtered_df['Low'].min():.2f}"
        )

    # Display raw data if desired
    if st.checkbox('Show Raw Data'):
        st.dataframe(filtered_df)

except Exception as e:
    st.error(f"Error loading data for {ticker}. Please check if the ticker symbol is correct.")
    st.exception(e)

# Footer
st.markdown("---")
st.markdown("Data provided by Yahoo Finance")
