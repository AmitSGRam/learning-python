def make_pizza(*toppings, size):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")
    
#make_pizza("mushrooms", "pepperoni", "cheese pizza", size=16)