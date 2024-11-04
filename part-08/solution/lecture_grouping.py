# TODO: Load the employees.csv again into a DataFrame
# First, group by the "Position" column and count the employees per position
# Then, group by the "Department" column and calculate the mean of all other columns per department

import pandas as pd
df = pd.read_csv("part-08/data/employees.csv")

# Your code here

print("Employees per position:")
print(df.groupby("Position").count())

print("Sum of all other columns per department:")
numeric_cols = df.select_dtypes(include=['number']).columns
print(df.groupby("Department")[numeric_cols].mean())
