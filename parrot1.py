p = "\nTell me something, and I will repeat it back to you:"
p += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
	message=input(p)
	if message != 'quit':
		print(message)