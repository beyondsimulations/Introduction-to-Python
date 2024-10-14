# a) TODO: Modify the previous function to handle both ZeroDivisionError and TypeError

def safe_divide_v2(add_1, add_2, div):
    try:
        result = (add_1 + add_2) / div
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input types"

# Test cases
print(safe_divide_v2(5, 5, 2))  # Should print: 5.0
print(safe_divide_v2(10, 0, 0))  # Should print: "Error: Division by zero"
print(safe_divide_v2(2, 4, "2"))  # Should print: "Error: Invalid input types"

# b) TODO: Write a function that asks the user for a number and then divides it by a second number inputted by the user.
# - Use a try-except block to handle the exceptions.
# - Use a while loop to repeatedly ask the user for a number and divide it by a second number until 
# the user inputs "no" to the question "Do you want to continue?".

def user_division():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Division by zero")
        except ValueError:
            print("Error: Invalid input. Please enter numbers only.")
        
        continue_input = input("Do you want to continue? (yes/no): ").lower()
        if continue_input != "yes":
            break

# Call the function to start the user input loop
user_division()
