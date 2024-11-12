import matplotlib.pyplot as plt
import numpy as np

# Set the style
plt.style.use('default')
fig, ax = plt.subplots(figsize=(12, 7))
fig.set_facecolor('#f8f9fa')
ax.set_facecolor('#ffffff')

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create plots with modern styling
ax.plot(x, y1, label="Sine", color='#4361ee', linewidth=2.5)
ax.plot(x, y2, label="Cosine", color='#f72585', linewidth=2.5)

# Customize the plot with modern aesthetics
ax.set_title('Sine and Cosine Functions', fontsize=16, pad=20, fontweight='bold')
ax.set_xlabel('x', fontsize=12, labelpad=10)
ax.set_ylabel('y', fontsize=12, labelpad=10)

# Improve grid and spines
ax.grid(True, linestyle='--', alpha=0.3, color='#666666')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Enhanced legend
ax.legend(fontsize=11, framealpha=0.95, loc='upper right')

# Add a slight margin to the plot
ax.margins(x=0.02)

# Adjust layout and display
plt.tight_layout()
plt.show()
plt.show()