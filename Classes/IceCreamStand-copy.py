#from restaurant import *
from restaurant import Restaurant as res_class

class IceCreamStand(res_class):

    def __init__(self, icecream_order='no'):
        super().__init__(restaurant_name, cuisine_type)
        self.order_att = IceCreamOrder(['Vanilla','Chocolate','Strawberry'], 7, icecream_order)

class IceCreamOrder:

    def __init__(self, flavors, order_count, icecream_order):
        """Initialize the IceCreamOrder's attributes."""
        self.flavors = flavors
        self.order_count = order_count
        self.icecream_order = icecream_order.lower()

    def get_icecream_or_not(self):
        """Check whether the customer wants an icecream or not"""
        if self.icecream_order == 'yes':
            print(f"The customer would like to buy an icecream.")
        elif self.icecream_order == 'no':
            print(f"The customer would not buy an icecream.")

    def get_flavors(self):
        """Print a statement describing the icecream flavors."""
        print(f"\nYour flavors: {self.flavors}.")

    def get_number_of_orders(self):
        """Print the number of ice creams ordered"""
        print(f"\nYour order count: {self.order_count}")

some_order = IceCreamStand("Yes")
some_order.describe_restaurant()
some_order.open_restaurant()
some_order.set_number_served(35)
"""
some_order = IceCreamStand("Japanese Restaurant", "Sushi","Yes")
other_order = IceCreamStand("Polish Restaurant", "Pierogi")

print(f"\nRestaurant of his choice is: {some_order.first}")
print(f"our order is: {some_order.second}")
some_order.describe_restaurant()
some_order.open_restaurant()
some_order.set_number_served(35)
print(f"Number of customers served: {some_order.number_served}")
some_order.increment_number_served(40)
print(f"Number of customers served: {some_order.number_served}")
some_order.order_att.get_flavors()
some_order.order_att.get_icecream_or_not()
some_order.order_att.get_number_of_orders()

print("\n")

print(f"\nRestaurant of his choice is: {other_order.first}")
print(f"other order is: {other_order.second}")
other_order.describe_restaurant()
other_order.open_restaurant()
other_order.set_number_served(35)
print(f"Number of customers served: {other_order.number_served}")
other_order.increment_number_served(40)
print(f"Number of customers served: {other_order.number_served}")
other_order.order_att.get_flavors()
other_order.order_att.get_icecream_or_not()
other_order.order_att.get_number_of_orders()
"""