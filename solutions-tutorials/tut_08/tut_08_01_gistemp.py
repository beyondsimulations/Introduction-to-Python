import pandas as pd
import matplotlib.pyplot as plt

# First, we load the NASA GISTEMP dataset for global temperature anomalies.
url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
temp_anomaly_data = pd.read_csv(url, skiprows=1) # skiprows=1 ensures that the first column is not read as a row index

# Convert all numeric columns (except 'Year') to float, replacing '***' with NaN
numeric_columns = temp_anomaly_data.columns.drop('Year')
temp_anomaly_data[numeric_columns] = temp_anomaly_data[numeric_columns].replace('***', float('nan')).astype(float)


# TODO: a) Display the first 5 rows to learn basic information about the DataFrame. For your work, you only need the 'Year' and and the data from all months. Drop the rest of the columns.
# Your code here
temp_anomaly_data = temp_anomaly_data.drop(columns=['J-D', 'D-N','DJF','MAM','JJA','SON'])
print(temp_anomaly_data.head())

# TODO: b) Calculate and print the average temperature anomaly for each year.
# Hint: To do so, you first need to pd.melt()` the DataFrame to convert months to a single column.
# Your code here
melted_data = pd.melt(temp_anomaly_data, id_vars=['Year'], var_name='Month', value_name='Anomaly')
yearly_avg = melted_data.groupby('Year')['Anomaly'].mean()
print("Average temperature anomaly for each year:")
print(yearly_avg)

# TODO: c) Find the year with the highest temperature anomaly and the year with the lowest.
# Hint: Use the `idxmax()` and `idxmin()` methods
# Your code here
max_year = yearly_avg.idxmax()
min_year = yearly_avg.idxmin()
print(f"Year with highest anomaly: {max_year}")
print(f"Year with lowest anomaly: {min_year}")

# TODO: d) Save the melted DataFrame to a Excel file with the name 'temp_anomaly_data.xlsx' for next lecture.
# Your code here
melted_data.to_excel('solutions-tutorials/tut_08/temp_anomaly_data.xlsx', index=False)
print("\nData saved to 'temp_anomaly_data.xlsx'")
