# TODO: Try to extract all dates in the text below:
text = """
Here is a date: 12.03.2024. Here is another one: 01/01/2024. And here is the third one: 01-01-2024.
Let's add more: 15-04-2023, 16/05/2023, and 17.06.2023. 
In July, we have 18/07/2023 and 19-07-2023. 
August brings us 20.08.2023 and 21/08/2023. 
September dates include 22-09-2023 and 23.09.2023. 
October has 24/10/2023 and 25-10-2023. 
November features 26.11.2023 and 27/11/2023. 
Finally, December rounds out the year with 28-12-2023 and 29.12.2023.

Continuing with more dates: 
01-01-2025, 02/02/2025, 03.03.2025, 04-04-2025, 05/05/2025, 06.06.2025, 
07-07-2025, 08/08/2025, 09.09.2025, 10-10-2025, 11/11/2025, 12.12.2025.

Even more dates: 
13-01-2026, 14/02/2026, 15.03.2026, 16-04-2026, 17/05/2026, 18.06.2026, 
19-07-2026, 20/08/2026, 21.09.2026, 22-10-2026, 23/11/2026, 24.12.2026.

And some more: 
25-01-2027, 26/02/2027, 27.03.2027, 28-04-2027, 29/05/2027, 30.06.2027, 
01-07-2027, 02/08/2027, 03.09.2027, 04-10-2027, 05/11/2027, 06.12.2027.
"""

# Your code here

import re

# Define the regex pattern to match all date formats
date_pattern = r'\d{2}[-./]\d{2}[-./]\d{4}'

# Find all matches in the text
dates = re.findall(date_pattern, text)

# Print the extracted dates
print("Extracted dates:")
for date in dates:
    print(date)

# Print the total number of dates found
print(f"\nTotal dates found: {len(dates)}")