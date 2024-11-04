# TODO: Load the employees.csv located in the git repository into a DataFrame
# First, filter the DataFrame for employees with a manager position
# Then, print the average salary of the remaining employees
# Finally, print the name of the employee with the lowest salary

import pandas as pd

df = pd.read_csv("part-08/data/employees.csv")

df = df[df["Position"] != "Manager"]

print("Filtered DataFrame:")
print(df.head())

print("Average salary:")
print(df["Salary"].mean())

df = df[df["Salary"] == df["Salary"].min()]

print("Highest paid employee:")
print(df["Name"])
