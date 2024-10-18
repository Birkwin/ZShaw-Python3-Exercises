from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

# Open the input file and get its data
in_data = open(from_file).read()

# Copy it to the destination
open(to_file, 'w').write(in_data)

print("Alright, all done.")

# Alternatively, this can all be done on one line
# open(to_file, 'w').write(open(from_file).read())
