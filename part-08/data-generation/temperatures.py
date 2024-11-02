import pandas as pd
import numpy as np

# Create dates for 3 months
dates = pd.date_range('2024-03-01', periods=92)  # March through May

# Create seasonal temperature progression (slightly warming as we move into spring)
hamburg_temps = np.concatenate([
    np.random.uniform(5, 12, 31),    # March (cooler)
    np.random.uniform(8, 15, 30),    # April (mild)
    np.random.uniform(12, 20, 31)    # May (warmer)
]).round(1)

la_temps = np.concatenate([
    np.random.uniform(15, 23, 31),   # March
    np.random.uniform(17, 25, 30),   # April
    np.random.uniform(19, 27, 31)    # May
]).round(1)

tokyo_temps = np.concatenate([
    np.random.uniform(10, 18, 31),   # March
    np.random.uniform(14, 21, 30),   # April
    np.random.uniform(18, 25, 31)    # May
]).round(1)

# Create DataFrame
temperatures = pd.DataFrame({
    'Date': dates,
    'Hamburg': hamburg_temps,
    'Los_Angeles': la_temps,
    'Tokyo': tokyo_temps
})

# Save to Excel file
temperatures.to_excel('temperatures.xlsx', index=False)

print("First few rows of the dataset:")
print(temperatures.head())