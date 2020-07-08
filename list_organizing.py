#sorting a list permanently
cars=['bmw','ferrari','lamborghini','ford','dodge','toyata','porche']
cars.sort()
print(cars)

#sorting a list TEMPORARILY
cars=['bmw','ferrari','lamborghini','ford','dodge','toyata','porche']
print(f'\nThe original list is: \n{cars}')
print(f'\nThe sorted list is:\n{sorted(cars)}')
print(f'\n\tHere is the Original list again!!!:\n\t{cars}')
cars.reverse()
print(f'\nDescending order of the list of cars is:\n{cars}')
print(f'\nThe total number of cars in the list is\t{len(cars)}')