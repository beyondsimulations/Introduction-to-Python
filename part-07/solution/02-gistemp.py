# In this exercise, you'll use Pandas to analyze real global temperature anomaly data from NASA, helping to understand trends in climate change over time.

# The dataset is provided by the GISS Team, 2024: GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies. Dataset at https://data.giss.nasa.gov/gistemp/.

import pandas as pd
import matplotlib.pyplot as plt

# First, we load the NASA GISTEMP dataset for global temperature anomalies.
url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
temp_anomaly_data = pd.read_csv(url, skiprows=1) # skiprows=1 ensures that the first column is not read as a row index
# Convert 'Anomaly' column to float
melted_data['Anomaly'] = melted_data['Anomaly'].astype(float)


# a) Display the first 5 rows and keep only 'Year' and month columns
temp_anomaly_data = temp_anomaly_data.drop(columns=['J-D', 'D-N','DJF','MAM','JJA','SON'])
print(temp_anomaly_data.head())

# b) Calculate and print the average temperature anomaly for each year
melted_data = pd.melt(temp_anomaly_data, id_vars=['Year'], var_name='Month')
melted_data = melted_data.drop(columns=['Month'])
print(melted_data.head())
melted_data.groupby(['Year']).mean()
print(melted_data.head())
print("\nAverage temperature anomaly for each year:")
print(melted_data.head())

# c) Find the year with the highest and lowest temperature anomaly
max_year = yearly_avg.idxmax()
min_year = yearly_avg.idxmin()
print(f"\nYear with highest anomaly: {max_year} ({yearly_avg[max_year]:.2f})")
print(f"Year with lowest anomaly: {min_year} ({yearly_avg[min_year]:.2f})")

# d) Create 'Anomaly_Category' column
def categorize_anomaly(value):
    if value < -0.2:
        return 'Cool'
    elif value > 0.2:
        return 'Warm'
    else:
        return 'Neutral'

melted_data['Anomaly_Category'] = melted_data['Anomaly'].apply(categorize_anomaly)

# e) Calculate the percentage of 'Warm' months for each decade
melted_data['Decade'] = (melted_data['Year'] // 10) * 10
warm_percentage = melted_data.groupby('Decade')['Anomaly_Category'].apply(lambda x: (x == 'Warm').mean() * 100)
print("\nPercentage of 'Warm' months for each decade:")
print(warm_percentage)

# f) Save the DataFrame to Excel
melted_data.to_excel('temp_anomaly_data.xlsx', index=False)
print("\nData saved to 'temp_anomaly_data.xlsx'")
