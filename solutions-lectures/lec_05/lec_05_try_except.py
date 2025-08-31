# Implement a function that converts a string to an integer
# 1. Try to convert the input_string to an integer
# 2. If successful, return the integer
# 3. If a ValueError occurs, catch it and return "Invalid input: not a number"
# 4. If any other exception occurs, catch it and return 
# "An unexpected error occurred: [type of exception]"

def string_to_int(input_string):
    try:
        return int(input_string)
    except ValueError:
        return "Invalid input: not a number"
    except Exception as e:
        return f"An unexpected error occurred: {type(e).__name__}"

# Test cases
print(string_to_int("42"))        # Should print: 42
print(string_to_int("Hello"))     # Should print: Invalid input: not a number
print(string_to_int([123]))       # Should print: An unexpected error occurred: TypeError  