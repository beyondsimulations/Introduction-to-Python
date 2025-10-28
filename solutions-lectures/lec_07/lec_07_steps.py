# Your daily step counts for one week
import numpy as np

steps = np.array([8500, 12000, 6800, 9500, 11200, 15000, 7800])
days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
target = 10000  # Daily step goal

# TODO: Find days where you exceeded your target (>= 10000 steps)
success_days = days[steps >= target]

# TODO: Print the successful days using fancy indexing
print(success_days)

# TODO: Calculate your weekly achievement rate (percentage of successful days)
achievement_rate = len(success_days) / len(days) * 100
print(f"Weekly achievement rate: {achievement_rate:.2f}%")
