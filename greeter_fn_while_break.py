def format1(f,l):
	full=f"{f} {l}"
	return full.title()
while True:
	print("enter name:")
	print("(enter 'quit' to quit)")
	f=input('first name:')
	if f == 'quit':
		break
	l=input('last name:')
	if l == 'quit':
		break	
	name=format1(f,l)
	print(name)
	