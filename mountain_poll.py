responses={}
#set a flag to indicate that polling is active
polling_active=True
while polling_active:	#prompt for the person's name and response
	name=input(f"\nWhat is your name?")
	response=input("Which mountain would you like to climb someday?")
	responses[name]=response
	repeat=input("Would you like to let another person respond?(Yes/No)")	#store the response in the dictionary
	if repeat == 'no':
		polling_active=False
print("\n---Polling Results---")
for name,response in responses.items():
	print(f"{name} would like to climb {response}")