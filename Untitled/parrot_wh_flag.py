prompt = "\nTell me something, and I will repeat it back to ya"
prompt += "\nEnter 'quit' to end the program. "
"""setting a flag"""
active = True

message = ""
while message != 'quit':
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)