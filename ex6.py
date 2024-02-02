# Define an integer var and format it into a string 'x'
types_of_people = 10
x = f"There are {types_of_people} types of people."

# Define two strings and format it into a string 'y'
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print both x and y to the terminal
print(x)
print(y)

# Print the previous vars again, but formatted into a new statement
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Set a boolean and create a string with aspace dedicated to be formatted
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Print the string that wasn't formatted and format it in the same line with the boolean
print(joke_evaluation.format(hilarious))

# Define two strings
w = "This is the left side of... "
e = "a string with a right side."

# Print both strings, one appended to the other
print(w + e)