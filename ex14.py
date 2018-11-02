from sys import argv

script, user_name = argv
#prompt = '> '
prompt = f'{script}> '

print(f"Hi {user_name}, I`m the {script} script.")
print("I`d like to like you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"how old are you {user_name}?")
age = int(input(prompt))
#always transform the type ealy so that you can find where is wrong early
#don`t do
#age = input(promt)
#print(f"You are {int(age)} years old.What kind of computer do you have?")
print(f"You are {age} old.What kind of computer do you have?")
computer = input(prompt)

#print("What kind of computer do you have?")
#computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.No sure where that is.
And you have a {computer} computer.Nice
""")
