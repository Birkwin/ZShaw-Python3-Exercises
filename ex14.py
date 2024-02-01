# Import arguments module
from sys import argv

# Grab script name and 2 extra arguments
script, user_name, alt_arg = argv
# Prompt name
prompt = '> '

# Print strings using the users name and ask a series of questions
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# Print several lines, including that second extra argument
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
Oh, and that extra argument you gave was {alt_arg}. Thanks for that.
""")