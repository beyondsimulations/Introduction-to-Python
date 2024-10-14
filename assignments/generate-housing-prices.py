import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate data
n_samples = 1000
data = {
    'Price': np.random.lognormal(mean=12.5, sigma=0.4, size=n_samples) * 1000,  # Price in Euros
    'Area': np.random.lognormal(mean=4.5, sigma=0.3, size=n_samples),
    'Rooms': np.random.randint(1, 6, n_samples),
    'Year_Built': np.random.randint(1900, 2023, n_samples),
    'Distance_to_Center': np.random.lognormal(mean=1.5, sigma=0.5, size=n_samples)
}

# Create DataFrame
df = pd.DataFrame(data)

# Adjust prices based on factors
df['Price'] *= np.sqrt(df['Area']) / 10
df['Price'] *= (df['Rooms'] ** 0.2)
df['Price'] *= (1 - (2023 - df['Year_Built']) * 0.005)  # Slight decrease for older buildings
df['Price'] *= (1 - df['Distance_to_Center'] * 0.015)  # Slight decrease for properties farther from center
df['Price'] /= 300

# Round and adjust data types
df['Price'] = df['Price'].round(-3)  # Round to nearest thousand
df['Area'] = df['Area'].round().astype(int)
df['Distance_to_Center'] = df['Distance_to_Center'].round(1)

# Add some missing values
df.loc[np.random.choice(df.index, 50), 'Year_Built'] = np.nan
df.loc[np.random.choice(df.index, 50), 'Distance_to_Center'] = np.nan

# Save to CSV
df.to_csv('assignments/hamburg_housing_prices.csv', index=False)
print("Dataset created and saved as 'hamburg_housing_prices.csv'")

# Display first few rows and data info
print(df.head())
print(df.info())