# TODO: Implement a new password strength checker
# Check for:
# - Minimum length of 8 characters
# - At least one uppercase letter
# - At least one lowercase letter
# - At least one digit
# - At least one special character (!@#$%^&*)
# Return "Weak" if no criteria is met, "Medium" if at least 3 criteria are met, "Strong" if all criteria are met

# Test your function
#print(check_password_strength("abc123"))
#print(check_password_strength("Str0ngP@ssw0rd"))

import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    
    criteria = [
        r'[A-Z]',  # Uppercase letter
        r'[a-z]',  # Lowercase letter
        r'\d',     # Digit
        r'[!@#$%^&*]'  # Special character
    ]
    
    strength = sum(bool(re.search(pattern, password)) for pattern in criteria)
    
    if strength == 4:
        return "Strong"
    elif strength >= 2:
        return "Medium"
    else:
        return "Weak"

# Test cases
print(check_password_strength("abc123"))  # Should return "Weak"
print(check_password_strength("Str0ngP@ssw0rd"))  # Should return "Strong"
print(check_password_strength("Password123"))  # Should return "Medium"
