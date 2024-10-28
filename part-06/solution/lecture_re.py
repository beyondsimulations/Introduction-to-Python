# Replace all occurrences of the word "Python" with "SECRET" in the following string.
import re
string = """
Python is a programming language. 
Python is also a snake. 
Monty Python was a theater group.
"""

print(re.sub(r'Python', 'SECRET', string))