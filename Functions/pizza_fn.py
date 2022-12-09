def make_pizza(*toppings):
    """print a list of toppings that have been requested."""
    #print(toppings)
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms','extra cheese','green peppers')