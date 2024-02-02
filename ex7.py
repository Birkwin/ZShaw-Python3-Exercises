# Print a string to commandd line
print("Mary had a little lamb.")
# Print a string with space that hasn't been formatted yet, and format it after the fact.
print("Its fleece was white as {}.".format('snow'))
# Print the same character 10 times
print("." * 10) # what'd that do?

# Set a host of variables equal to a series of characters
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch end = ' ' at the end. Try removing it to see what happens.
# The ' ' ensures that we're still printing on the same line, instead of getting a new one.
# This code prints each variable next to each other, without spaces added in, must be done automatically.
print(end1 + end2 + end3 + end4 + end5 + end6, end= ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
