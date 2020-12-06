#Passing an arbitrary number of arguments
def make_pizza(*toppings):
	print(f"Your toppings:")
	for topping in toppings:	
		print(f"- {topping.title()}")
make_pizza('pepperoni')
make_pizza('pepperoni','green peppers','extra cheese')