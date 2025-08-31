# Temperature classification

while True:
    # Ask user for temperature
    temperature = float(input("Enter a temperature: "))

    # Classify the temperature
    if temperature < 0:
        classification = "Freezing"
    elif 0 <= temperature <= 10:
        classification = "Cold"
    elif 11 <= temperature <= 20:
        classification = "Cool"
    elif 21 <= temperature <= 30:
        classification = "Warm"
    else:
        classification = "Hot"

    # Print the classification
    print(f"The temperature is {classification}.")

    # Ask if the user wants to continue
    continue_program = input("Do you want to continue? (yes/no): ").lower()
    if continue_program != "yes":
        break

print("Program ended.")

# Check the different temperatures by running the code with different inputs.