dates = """
On 07-04-1776, the United States declared its independence. Many years later, 
on 11-09-1989, the Berlin Wall fell. In more recent history, the COVID-19 
pandemic was declared a global emergency on 04-11-2020.
"""
# Try to find all dates in the above text with findall()
# Your code here

import re

print(re.findall(r'\d{2}-\d{2}-\d{4}', dates))