# TODO: Load and transform the temperatures.xlsx file by melting it
# Expected output format:
#         Date        City  Temperature
# 0  2024-03-01    Hamburg         7.2
# 1  2024-03-01 Los_Angeles       18.5
# 2  2024-03-01      Tokyo        12.3
# Then, print the maximum temperature per city by grouping by the "City" column

import pandas as pd

df = pd.read_excel("part-08/data/temperatures.xlsx", sheet_name="Temperatures")
df = pd.melt(df, id_vars=["Date"], var_name="City", value_name="Temperature")
print("Maximum temperature per city:")
print(df.groupby("City")["Temperature"].max())
