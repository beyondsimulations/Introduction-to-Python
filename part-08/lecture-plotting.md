---
title: "Lecture VIII - Data Visualization"
subtitle: "Programming with Python"
author: "Dr. Tobias Vlćek"
institute: "Kühne Logistics University Hamburg - Fall 2024"
title-slide-attributes:
    data-background-color: "#FFE0D3"

execute:
    echo: true

  render:
    - 404.qmd
    - index.qmd
    - general/*.qmd
    - part-01/*.qmd
    - part-02/*.qmd
    - part-03/*.qmd
    - part-04/*.qmd
    - part-05/*.qmd
    - part-06/*.qmd
    - part-07/*.qmd

format:
    revealjs:
        theme: [default, ../styles.scss]
        transition: slide
        transition-speed: fast
        highlight-style: arrow
        code-overflow: wrap
        slide-number: true
        code-copy: true
        code-link: true
        preview-links: auto
        footer: " {{< meta title >}} | {{< meta author >}} | [Home](lecture-plotting.qmd)"
        output-file: lecture-plotting-presentation.html
    html:
        theme: litera
        highlight-style: arrow
        code-overflow: wrap
        linkcolor: "#a60000"
        slide-number: true
        code-copy: true
        code-link: true
        toc: true
        toc-location: right
    pdf: 
        documentclass: report
        geometry:
            - margin=1in
        fontfamily: roboto
        fontfamilyoptions: sfdefault
        colorlinks: true
---

# [Quick Recap of the last Lecture]{.flow} {.title}

## NumPy: Efficient Computations

- Fundamental package for [scientific computing]{.highlight} in Python
- Support for large, multi-dimensional arrays and matrices
- [Wide range]{.highlight} of mathematical functions for arrays:
  - Fast array operations
  - Broadcasting capabilities
  - Linear algebra functions
  - Random number generation

## Pandas: Data Analysis

- Powerful library for [data manipulation and analysis]{.highlight}
- Built on top of NumPy, providing additional functionality
- Key features of Pandas include:
  - Data loading from various file formats
  - Data cleaning and preprocessing
  - Powerful grouping and aggregation operations
  - Merging and joining datasets (not covered!)

## Why NumPy and Pandas are Essential

- Basic tools for [scientific computing]{.highlight} and [data analysis]{.highlight}
- [Efficient data structures]{.highlight} and operations for large data
- Integration with other scientific Python libraries
- Used in data science, machine learning, and research

. . .

::: {.callout-tip}
You might also need them in future lectures here!
:::

# [Data Visualization]{.flow} {.title}

##

::: {.r-fit-text}

[Question:]{.question} What is

data visualization?

:::

## Visual Representations of Data

```{python}
#| code-fold: true

import matplotlib.pyplot as plt
import numpy as np


# Generate data
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = 3 + 2*x + np.random.randn(50)
sizes = np.random.randint(20, 200, 50)
colors = np.random.rand(50)

# Create the plot
plt.figure(figsize=(12, 5))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')

# Add trend line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2)

# Customize the plot
plt.title("ScatterPlot with Trend Line", fontsize=16)
plt.xlabel("X-axis", fontsize=12)
plt.ylabel("Y-axis", fontsize=12)
plt.colorbar(scatter, label="Color Scale")

# Add a text annotation
plt.annotate("Interesting point", xy=(8, 21), xytext=(6.5, 23),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## Importance of Data Visualization

- [Communicates]{.highlight} complex information clearly
- Helps in [decision-making]{.highlight} processes
- Reveals hidden patterns and relationships in data
- Makes data more [accessible]{.highlight} and engaging

::: {.callout-tip}

Helps to [convice]{.highlight} stakeholders!

:::

# [Common Types of Data Visualizations]{.flow} {.title}

## Bar Charts and Histograms

- Bar charts: Compare quantities across categories
- Histograms: Show distribution of a continuous variable

```{python}
#| code-fold: true
import matplotlib.pyplot as plt
import numpy as np

# Bar chart
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 2, 8]

plt.figure(figsize=(10, 3))
plt.subplot(121)
plt.bar(categories, values)
plt.title('Bar Chart')

# Histogram
data = np.random.randn(1000)

plt.subplot(122)
plt.hist(data, bins=30)
plt.title('Histogram')

plt.tight_layout()
plt.show()
```

## Line Charts and Area Charts

- Line charts: Show trends over time or continuous data
- Area charts: Similar to line charts, but with filled areas

```{python}
#| code-fold: true
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 3))
plt.subplot(121)
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Line Chart')
plt.legend()

plt.subplot(122)
plt.fill_between(x, y1, label='sin(x)')
plt.fill_between(x, y2, label='cos(x)', alpha=0.5)
plt.title('Area Chart')
plt.legend()

plt.tight_layout()
plt.show()
```

## Scatter Plots and Bubble Charts

- Scatter plots: Show relationship between two variables
- Bubble charts: Adds dimension with varying point sizes

```{python}
#| code-fold: true
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 500

plt.figure(figsize=(10, 3))
plt.subplot(121)
plt.scatter(x, y)
plt.title('Scatter Plot')

plt.subplot(122)
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.title('Bubble Chart')

plt.tight_layout()
plt.show()
```

## Pie Charts and Donut Charts

- Pie charts: Show composition of a whole
- Donut charts: Similar to pie charts, but with a hole in the center

```{python}
#| code-fold: true
import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]

plt.figure(figsize=(10, 3))

# Pie chart (left subplot)
plt.subplot(121)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')

# Donut chart (right subplot)
plt.subplot(122)
plt.pie(sizes, labels=labels, autopct='%1.1f%%', 
        pctdistance=0.7, labeldistance=1.1,
        wedgeprops=dict(width=0.5, edgecolor='white'))
plt.title('Donut Chart')

plt.tight_layout()
plt.show()
```

## Heatmaps and Choropleth Maps

- Heatmaps: Show intensity of data using color scales
- Choropleth maps: Geographical colored areas 

## Box Plots and Violin Plots

- Box plots: Show distribution of data through quartiles
- Violin plots: Combine box plot with kernel density

```{python}
#| code-fold: true
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 5)]

plt.figure(figsize=(10, 3))
plt.subplot(121)
plt.boxplot(data)
plt.title('Box Plot')

plt.subplot(122)
sns.violinplot(data=data)
plt.title('Violin Plot')

plt.tight_layout()
plt.show()
```

## Network Graphs and Trees

- Network graphs: Show relationships between entities
- Tree diagrams: Display hierarchical structures

```{python}
#| code-fold: true
import matplotlib.pyplot as plt
import networkx as nx

# Network graph
G = nx.random_geometric_graph(20, 0.3)

plt.figure(figsize=(10, 3))
plt.subplot(121)
nx.draw(G, with_labels=True)
plt.title('Network Graph')

# Tree diagram
T = nx.random_tree(10)

plt.subplot(122)
pos = nx.spring_layout(T)
nx.draw(T, pos, with_labels=True)
plt.title('Tree Diagram')

plt.tight_layout()
plt.show()
```

## Sankey Diagrams

- Show flows between nodes
- Useful for visualizing complex systems

```{python}
#| code-fold: true
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A", "B", "C", "D", "E", "F"],
      color = "blue"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3],
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2]
  ))])

fig.update_layout(title_text="Sankey Diagram Example", font_size=10)
fig.show()
```

## Ridgeline Plots

- Show distribution of data across categories

```{python}
#| code-fold: true
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Create sample data
np.random.seed(0)
num_points = 500
num_distributions = 5

data = []
for i in range(num_distributions):
    distribution = stats.norm.rvs(loc=i, scale=1, size=num_points)
    data.append(pd.DataFrame({'value': distribution, 'group': f'Group {i+1}'}))

df = pd.concat(data, ignore_index=True)

# Create the ridgeline plot
plt.figure(figsize=(10, 6))
for i, group in enumerate(df['group'].unique()):
    group_data = df[df['group'] == group]['value']
    sns.kdeplot(data=group_data, shade=True, alpha=0.7, y=i, clip=(0, 10))

plt.yticks(range(num_distributions), df['group'].unique())
plt.title('Ridgeline Plot Example')
plt.xlabel('Value')
plt.ylabel('Group')
plt.show()
```

# [Beautiful Plotting]{.flow} {.title}

- There are many libraries for data visualization in Python
- Some of the most popular libraries are:
    - Matplotlib
    - Seaborn
    - Plotly
    - Bokeh
    - Altair
    - GeoPandas
    - Geoplot
    - Geoplotlib

# [Matplotlib Module]{.flow} {.title}

- Matplotlib is the foundation for most Python plotting libraries
- Provides a MATLAB-like plotting interface
- Highly customizable and suitable for publication-quality figures

## Basic Matplotlib Example

```{python}
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.show()
```

```{python}
# [Matplotlib Module]{.flow} {.title}

# [Seaborn Module]{.flow} {.title}

# [Plotly Module]{.flow} {.title}

# [Dash Module]{.flow} {.title}

# [Bokeh Module]{.flow} {.title}

```

```
import geopandas as gpd
import matplotlib.pyplot as plt
from geodatasets import get_path

# Load the NYC Airbnb dataset
airbnb = gpd.read_file(get_path("nyc_airbnb"))

# Group by neighborhood and calculate mean price
neighborhood_prices = airbnb.groupby('neighbourhood')['price'].mean().reset_index()

# Load NYC neighborhoods shapefile
nyc = gpd.read_file(get_path("nyc_neighborhoods"))

# Merge neighborhood prices with NYC shapefile
nyc = nyc.merge(neighborhood_prices, how='left', left_on='neighborhood', right_on='neighbourhood')

# Create the plot
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the choropleth
nyc.plot(column='price', ax=ax, legend=True,
         legend_kwds={'label': 'Average Airbnb Price ($)'},
         cmap='YlOrRd', missing_kwds={'color': 'lightgrey'})

# Remove axes
ax.axis('off')

# Add a title
plt.title('Average Airbnb Prices by Neighborhood in New York City', fontsize=16)

plt.tight_layout()
plt.show()
