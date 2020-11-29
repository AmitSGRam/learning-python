p="Enter the name of the city you have visited:"
p+="\n(Enter 'quit' when you are finished.)"
while True:
	city = input(p)
	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")