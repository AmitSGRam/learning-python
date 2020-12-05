#Passing a List
def greet(names):
	for name in names:
		msg=f"Hello, {name.title()}"
		print(msg)
username=['alice','beerus','cyrus']
greet(username)