from sys import argv   #importing argv module from sys library in python.
script, user_name = argv  #unpacking the command-line arguments.
prompt = '>'   #setting a symbol to the variable "prompt".
print(f"Hi {user_name}, I'm the {script} script.")   #accessing the value from command-line and along with script name using string formatting.
print("I'd like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes=input(prompt)          #takes input from the user.The line will begin with prompt symbol  ">" which we set early.
print(f"where do you live{user_name}?")
lives=input(prompt)
print("What kind of computer do you have?")
computer=input(prompt)
print(f"""Alright, so you said {likes} about liking me. You live in {lives}. Not sure where that is. And you have a {computer} computer. Nice.""")