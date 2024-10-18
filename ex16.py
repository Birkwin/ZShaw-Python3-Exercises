# Import libraries
from sys import argv
# First var is name of the script we're running, second is the variable we've chucked in
script, filename = argv

# Inform the user of what we're about to do, and give them the chance to cancel
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

# Open the file the user entered
print("Opening the file...")
# We need to be specific and add 'w' (write) as an option, otherwise the program
# Will be safe and not let us edit it
target = open(filename, 'w')

# Empties out all the contents of the file
print("Truncating the file. Goodbye!")
# Don't actually need this, as using the 'w'
# option already truncates the file!
target.truncate()

print("Now I'm going to ask you for three lines.")

# Ask for 3 lines to add to the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Go through and append all three lines to the document
target.write(f"{line1}\n{line2}\n{line3}\n")

# Close the document to free up memory
print("And finally, we close it.")
target.close()