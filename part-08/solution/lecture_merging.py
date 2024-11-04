import pandas as pd
df1 = pd.DataFrame({
    "Name": ["John", "Alice", "Bob", "Carol"],
    "Department": ["Sales", "IT", "HR", "Sales"],
    "Salary": [50000, 60000, 55000, 52000]})
df2 = pd.DataFrame({
    "Name": ["Alice", "Bob", "Dave", "Eve"],
    "Position": ["Developer", "Manager", "Analyst", "Developer"],
    "Years": [5, 8, 3, 4]})

# TODO: Merge the two DataFrames on the "Name" column
# Try different types of merges (inner, outer, left, right)
# Observe and describe the differences in the results

df_merged = df1.merge(df2, on="Name", how="inner")
print(df_merged)

df_merged = df1.merge(df2, on="Name", how="outer")
print(df_merged)

df_merged = df1.merge(df2, on="Name", how="left")
print(df_merged)

df_merged = df1.merge(df2, on="Name", how="right")
print(df_merged)
