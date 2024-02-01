from sys import argv
# Read the WYSS section for how to run this
# Unpacks arguments from command line and places them into variables in order
script, first, second, third = argv

# Take on last additional argument
fourth = input("Please choose a 4th input: ")

# Print out all of our arguments
print("\nThe script is called:", script)
print("Your first variable is called:", first)
print("Your second variable is:", second)
print("Your third variable is called:", third)
print("Your fourth variable is called:", fourth)