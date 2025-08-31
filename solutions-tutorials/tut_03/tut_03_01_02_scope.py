# b) TODO: Implement a function that uses a global variable to keep track of how many times it has been called.
# Call the functions 10 times and print the result to the console.

functions_called = 0

def count_calls():
    global functions_called
    functions_called += 1
    return functions_called

# Call the function 10 times and print the result
for _ in range(10):
    result = count_calls()
    print(f"Function called {result} times")