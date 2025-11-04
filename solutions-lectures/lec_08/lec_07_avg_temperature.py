# TODO: Load the temperatures.xlsx file into a DataFrame
# Look at the first few rows of the DataFrame
# Then, print the average temperature per city

import pandas as pd

df = pd.read_excel(
    "lectures/supplementary/lec_08/temperatures.xlsx", sheet_name="Temperatures"
)

print(df.head())
print("Average temperature in Hamburg:")
print(df["Hamburg"].mean())
print("Average temperature in Los Angeles:")
print(df["Los_Angeles"].mean())
print("Average temperature in Tokyo:")
print(df["Tokyo"].mean())
