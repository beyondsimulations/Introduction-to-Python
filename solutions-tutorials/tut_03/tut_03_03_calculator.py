# TODO: Create a function called 'advanced_calculator' that takes three parameters:
# - num1 (number)
# - num2 (number)
# - operation (string: "add", "subtract", "multiply", "divide", "power", "modulo")
# The function should:
# - Perform the requested operation
# - Handle division by zero (return "Error: Division by zero")
# - Return the result as a formatted string like "5 + 3 = 8"
# Your code here

def advanced_calculator(num1: int, num2: int, operation: str):
    if operation == "add":
        result = num1 + num2
        return f"{num1} + {num2} = {result}"

    elif operation == "subtract":
        result = num1 - num2
        return f"{num1} - {num2} = {result}"

    elif operation == "multiply":
        result = num1 * num2
        return f"{num1} * {num2} = {result}"

    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
        return f"{num1} / {num2} = {result}"

    elif operation == "power":
        result = num1 ** num2
        return f"{num1} ^ {num2} = {result}"

    elif operation == "modulo":
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 % num2
        return f"{num1} % {num2} = {result}"

    else:
        return f"Error: Invalid operation '{operation}'"


print(advanced_calculator(5,6,"divide"))
