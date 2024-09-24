def check_number():
    number = input("Which number?")
    number = int(number)
    if number > 0:
        return "positive"
    if number < 0:
        return "negative"
    
result = check_number()
print(result)