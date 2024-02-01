# Ask a question using a print string, then obtain an answer using input()
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

# Format a string that includes the users answers and print it
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("\nOnce more, please")

# Do the same as before, but ask the question and print the string all at once
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print(f"Ok, so you're {age} old, {height} tall and {weight} heavy.")