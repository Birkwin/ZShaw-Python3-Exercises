from sys import argv

# We need to pass a file into here!! Do this in the terminal when calling this script
# We get the input we used as the second output
script, filename = argv

# Open the file input, if the input is not correct we get errors
# Save to a variable
txt = open(filename)

# Print out the contents of the file
print(f"Here's your file {filename}:")
# Specifically here we read the contents of the file and pass that stream into the print command
print(txt.read())
# Close the variable to free up the memory
txt.close()

# Ask for user input to get the argv we supplied earlier
print("Type the filename again:")
file_again = input("> ")

# Attempt to read the new file
txt_again = open(file_again)

print(txt_again.read())
# Clear up memory
txt_again.close()
