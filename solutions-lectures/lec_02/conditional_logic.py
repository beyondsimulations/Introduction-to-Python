# Given a numerical score, classify it into letter grades
score = -100  # You can test with different values

# Your task: Create if/elif/else statements that assign letter grades:
# 90-100: "A"
# 80-89: "B"
# 70-79: "C"
# 60-69: "D"
# Below 60: "F"
# Also handle invalid scores (negative or > 100)

# Your code here
if score > 100:
    grade = "Can't grade as score is too high."
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 0:
    grade = "F"
else:
    grade = "Score too low to be graded."

print(f"Score: {score}, Grade: {grade}")
