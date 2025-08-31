# c) TODO: Create a function called password_strength that takes a password as input. 
# It should return "weak", "medium", or "strong" based on the passwords length with the following criteria:
# - Return "weak" if the password is less than 8 characters long
# - Return "medium" if the password is between 8 and 15 characters long
# - Return "strong" if the password is longer than 15 characters long
# - The function should then be called as illustrated below.

def password_strength(password):
    if len(password) < 8:
        return "weak"
    elif 8 <= len(password) <= 15:
        return "medium"
    else:
        return "strong"

# Your code here

password = input("Enter a password: ")
strength = password_strength(password)
print(f"The strength of the password is {strength}.")