import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for better visualization
plt.style.use('fivethirtyeight')

def simulate_stock_price(initial_price, days, daily_std):
    # Set up the plot
    plt.figure(figsize=(12, 6))
    
    # Generate 5 random walks
    colors = sns.color_palette("husl", 5)  # Get 5 distinct colors
    
    for i in range(5):
        # Generate random daily returns
        daily_returns = np.random.normal(0, daily_std, days)
        
        # Calculate price path
        price_path = initial_price * np.exp(np.cumsum(daily_returns))
        
        # Create time array
        time = np.arange(days)
        
        # Plot each path with a different color
        plt.plot(time, price_path, linewidth=2, color=colors[i], 
                label=f'Sim {i+1}', alpha=0.8)
        plt.fill_between(time, price_path, alpha=0.05, color=colors[i])
    
    plt.title('Stock Price Random Walk Simulations', fontsize=14, pad=15)
    plt.xlabel('Days', fontsize=12)
    plt.ylabel('Stock Price ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.show()

# Get user input
initial_price = float(input("Enter initial stock price: "))
days = int(input("Enter number of days to simulate: "))
daily_std = float(input("Enter daily standard deviation (e.g., 0.02 for 2%): "))

# Run simulation
simulate_stock_price(initial_price, days, daily_std)
