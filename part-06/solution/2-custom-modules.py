#| eval: false
# TODO: Create a new module called calculator.py
# The module should contain at least four functions: 
# add, subtract, multiply, and divide
# Afterward, the following code should work:

import calculator as calc

assert calc.add(2, 3) == 5
assert calc.subtract(5, 1) == 4
assert calc.multiply(4, 7) == 28
assert calc.divide(10, 2) == 5

print("Wonderful, all tests passed!")