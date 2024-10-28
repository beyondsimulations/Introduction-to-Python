# First, check if a directory called `module_directory` exists.
# If it does not, create it.
# Then, list all files in the current directory and save them in a CSV file called `current_files.csv` in the new `module_directory`.

import os
import csv

if not os.path.exists('part-06/module_directory'):
    os.makedirs('part-06/module_directory')

with open('part-06/module_directory/current_files.csv', 'w') as f:
    writer = csv.writer(f)
    for file in os.listdir():
        writer.writerow([file])