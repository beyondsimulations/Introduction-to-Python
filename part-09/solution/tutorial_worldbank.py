import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read and process data (same as before)
df = pd.read_csv('part-09/data/API_EG.FEC.RNEW.ZS_DS2_en_csv_v2_10215.csv', skiprows=4)
df_melted = df.melt(
    id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'],
    var_name='Year',
    value_name='Renewable Energy %'
)
df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce')
df_melted = df_melted.dropna(subset=['Year', 'Renewable Energy %'])

# Select countries and create plot data
countries = ['Norway', 'Brazil', 'Germany', 'China', 'United States', 'India']
df_plot = df_melted[df_melted['Country Name'].isin(countries)]

# Set the style and color palette
plt.style.use('seaborn-v0_8-darkgrid')
colors = sns.color_palette("husl", len(countries))

# Create figure with a specific background color
fig, ax = plt.subplots(figsize=(12, 7), facecolor='#f6f6f6')
ax.set_facecolor('#f6f6f6')

# Plot each country with custom styling
for i, country in enumerate(countries):
    country_data = df_plot[df_plot['Country Name'] == country]
    
    # Create the main line
    line = ax.plot(country_data['Year'], country_data['Renewable Energy %'],
            label=country, color=colors[i], linewidth=2.5)
    
    # Add subtle shadow effect
    ax.plot(country_data['Year'], country_data['Renewable Energy %'],
            color=colors[i], linewidth=4, alpha=0.1)
    
    # Add endpoint labels
    last_value = country_data.iloc[-1]['Renewable Energy %']
    ax.annotate(f'{country}: {last_value:.1f}%',
                xy=(2021, last_value),
                xytext=(5, 0),
                textcoords='offset points',
                va='center',
                color=colors[i],
                fontsize=9,
                fontweight='bold')

# Customize the plot
plt.title('Renewable Energy Consumption Trends\nby Major Economies (1990-2021)', 
          pad=20, fontsize=16, fontweight='bold')

plt.xlabel('Year', fontsize=12, labelpad=10)
plt.ylabel('Percentage of Total Energy Consumption', fontsize=12, labelpad=10)

# Customize grid
ax.grid(True, linestyle='--', alpha=0.7)

# Customize spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Customize ticks
plt.xticks(np.arange(1990, 2022, 5), fontsize=10)
plt.yticks(fontsize=10)

# Add subtle shading
ax.fill_between(df_plot['Year'].unique(), 
                ax.get_ylim()[0], 
                ax.get_ylim()[1], 
                where=df_plot['Year'].unique() % 10 == 0,
                color='gray', alpha=0.05)

# Add context
plt.figtext(0.10, 0.02,
            'Source: World Bank Development Indicators (2024)\nIndicator: Renewable energy consumption (% of total final energy consumption)',
            fontsize=6, style='italic', alpha=0.7)

# Adjust layout
plt.tight_layout()
plt.show()