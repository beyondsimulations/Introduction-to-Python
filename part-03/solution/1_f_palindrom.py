# f) TODO: Implement a function is_palindrome that checks if a given string is a palindrome (reads the same forwards and backwards).
# Hint: Remember how we can use slicing to reverse a string.
# Your code here

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # Should output True
print(is_palindrome("hello"))    # Should output False
