import numpy as np

# Let's analyze temperature data from 10 weather stations over 30 days
temp_data = np.random.randint(0, 40, size=(10, 30))

# Example: Calculate the average temperature for the first station
first_station_avg = np.mean(temp_data[0,:])
print(f"Average temperature for the first station: {first_station_avg:.2f}°C")

# TODO: a) Calculate the average temperature for each station and print it. Make sure to round the result to 2 decimal places!
# Hint: Use np.mean() and a for loop
# Your code here
for station in range(10):
    print(f"Average temperature for station {station}: {np.mean(temp_data[station,:]):.2f}°C")

# TODO: b) Find the highest temperature recorded and the station index and print it
# Hint: Use np.max() and np.argmax() 
# Your code here
print(f"Highest temperature recorded at station {np.argmax(temp_data)} with {np.max(temp_data)}°C")

# TODO: c) Find the lowest temperature recorded and the station index and print it
# Hint: Use np.min() and np.argmin()
# Your code here
print(f"Lowest temperature recorded at station {np.argmin(temp_data)} with {np.min(temp_data)}°C")

# TODO: d) Calculate the overall average temperature and print it
# Hint: Use np.mean() on the entire temp_data array and round the result to 2 decimal places
# Your code here
print(f"Overall average temperature: {np.mean(temp_data):.2f}°C")

# Example: Identify days above 30°C for the first station
hot_days = np.sum(temp_data[0,:] > 30)
print(f"The first station had {hot_days} days above 30°C")

# TODO: e) Count the number of days above 30°C for each station and print it in a nice format
# Hint: Use np.sum() with a condition and a for loop
# Your code here
for station in range(10):
    print(f"Station {station} had {np.sum(temp_data[station,:] > 30)} days above 30°C")

# TODO: f) Find the hottest and coldest stations and determine the index of the station with the highest average temperature and the station with the lowest average temperature. Print the results in a nice format including the index and the average temperature.
# Hint: Use np.argmax() and np.argmin(), the appropriate axis, and round the result to 2 decimal places
# Your code here
print(f"Hottest station: {np.argmax(np.mean(temp_data, axis=1))} with {np.max(np.mean(temp_data, axis=1)):.2f}°C")
print(f"Coldest station: {np.argmin(np.mean(temp_data, axis=1))} with {np.min(np.mean(temp_data, axis=1)):.2f}°C")
