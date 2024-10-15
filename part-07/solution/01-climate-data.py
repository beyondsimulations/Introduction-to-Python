#Imagine you're a climate scientist working on a project to analyze temperature data from weather stations across the country. You've been given a large dataset, and you need to use NumPy to process and analyze this data efficiently.

import numpy as np

# First, we simulate loading data from 100 weather stations over 365 days. Each row represents a station, each column a day.
temp_data = np.random.randint(0, 40, size=(100, 365))

# a) Calculate the average temperature for each station and the overall average temperature.
station_averages = np.mean(temp_data, axis=1)
overall_average = np.mean(temp_data)
print(f"Average temperature for each station:\n{station_averages}")
print(f"Overall average temperature: {overall_average:.2f}°C")

# b) Find the highest and lowest temperature recorded and print a message with the corresponding stations.
highest_temp = np.max(temp_data)
lowest_temp = np.min(temp_data)
highest_station, highest_day = np.where(temp_data == highest_temp)
lowest_station, lowest_day = np.where(temp_data == lowest_temp)
print(f"Highest temperature: {highest_temp}°C at station {highest_station[0]} on day {highest_day[0]}")
print(f"Lowest temperature: {lowest_temp}°C at station {lowest_station[0]} on day {lowest_day[0]}")

# c) Identify heat waves. A heat wave is defined as 5 consecutive days with temperatures above 30°C. Print a message counting the number of heat waves.
heat_waves = 0
for station in temp_data:
    consecutive_hot_days = 0
    for temp in station:
        if temp > 30:
            consecutive_hot_days += 1
            if consecutive_hot_days == 5:
                heat_waves += 1
                consecutive_hot_days = 0  # Reset to avoid double-counting
        else:
            consecutive_hot_days = 0
print(f"Total number of heat waves across all stations: {heat_waves}")


# d) Calculate the temperature anomaly for each day (difference from each individual station's average temperature).
temp_anomaly = temp_data - station_averages[:, None]
print("Temperature anomaly shape:", temp_anomaly.shape)

# e) Find the hottest and coldest stations and determine the index of the station with the highest average temperature and the station with the lowest average temperature.
hottest_station = np.argmax(station_averages)
coldest_station = np.argmin(station_averages)
print(f"Hottest station index: {hottest_station}, with average temperature: {station_averages[hottest_station]:.2f}°C")
print(f"Coldest station index: {coldest_station}, with average temperature: {station_averages[coldest_station]:.2f}°C")