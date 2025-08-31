# TODO: Write a function that asks the user for a username and then checks if the username is valid.
# - A valid username is considered to be a number that is at least 5 characters long and contains no spaces.
# - If the username is not valid, you should raise an exception, tell the user that the username is not valid and ask for a new username.
# - You should only accept the username if it is valid.


class InvalidUsernameError(Exception): # This is a custom exception that inherits from the built-in Exception class
    pass

def get_valid_username():
    while True:
        try:
            username = input("Please enter a username (at least 5 characters, numbers only): ")
            if len(username) < 5:
                raise InvalidUsernameError("Username must be at least 5 characters long.")
            if ' ' in username:
                raise InvalidUsernameError("Username cannot contain spaces.")
            for char in username:
                if char not in '0123456789':
                    raise InvalidUsernameError("Username must contain only numbers.")
            return username
        except InvalidUsernameError as e:
            print(f"Invalid username: {e}")
            print("Please try again.")

# Example usage
valid_username = get_valid_username()
print(f"Valid username entered: {valid_username}")