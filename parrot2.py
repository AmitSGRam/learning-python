p="\nTell me something, and I will repeat it back to you"
p+="\nEnter 'quit' to end the program."
active = True
while active:
	message=input(p)
	if message =='quit':
		active = False
	else:
		print(message)