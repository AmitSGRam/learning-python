#Mixing Positional and Arbitrary Argument
def make_pizza(size,*toppings):
	print(f"Making a {size} - inch pizza with the following toppings:")
	for topping in toppings:	
		print(f"- {topping.title()}")
make_pizza(16,'pepperoni')
make_pizza(12,'pepperoni','green peppers','extra cheese')