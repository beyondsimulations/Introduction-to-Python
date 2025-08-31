# TODO: Write a function that calculates the area of a rectangle. Ensure that the length and width are positive numbers.
def calculate_rectangle_area(length, width):
    # Assert that length and width are positive numbers
    assert isinstance(length, (int, float)) and length > 0, "Length must be a positive number"
    assert isinstance(width, (int, float)) and width > 0, "Width must be a positive number"
    
    # Calculate and return the area
    return length * width

# Test cases
print(calculate_rectangle_area(5, 3))    # Should print: 15
print(calculate_rectangle_area(-5, 3))   # Should raise AssertionError
print(calculate_rectangle_area(5, "3"))  # Should raise AssertionError