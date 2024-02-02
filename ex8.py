# Create an empty string with space to be formatted
formatter = "{} {} {} {}"

# Format the string with integers
print(formatter.format(1, 2, 3, 4))
# Format the string with strings
print(formatter.format("one", "two", "three", "four"))
# Format the string with booleans
print(formatter.format(True, False, True, False))
# Format the string with itself
print(formatter.format(formatter, formatter, formatter, formatter))
# Format the string with 4 large strings, seperated on different lines
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poen",
    "Or a song about fear"
))