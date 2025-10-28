# German grades: 1.0 (best) to 5.0 (worst), 4.0 is passing grade
import numpy as np

grades = np.array(
    [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.0, 2.3, 1.7, 2.0, 3.3, 2.7]
)

print("Student grades:", grades)

# TODO: Calculate and print the following statistics:
# - Class average
# - Standard deviation
# - Best grade
# - Worst grade
#
print("Class average:", np.mean(grades))
print("Standard deviation:", np.std(grades))
print("Best grade:", np.max(grades))
print("Worst grade:", np.min(grades))

# Your statistical analysis here
