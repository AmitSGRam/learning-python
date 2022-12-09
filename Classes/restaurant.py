class Restaurant:
    """A class to represent user's orders and restaurants of choice."""

    def __init__(self, restaurant_name, cuisine_type):
        self.first = restaurant_name
        self.second = cuisine_type
        self.number_served = 1
    
    def describe_restaurant(self):
        print(f"Ordering {self.number_served}-number of {self.second} from {self.first}.")

    def open_restaurant(self):
        print(f"Restaurant {self.first} is now open.")

    def set_number_served(self, count):
        self.number_served = count

    def increment_number_served(self, new_count):
        """Add the new count to the number of customers served."""
        self.number_served += new_count

my_order = Restaurant("McDonalds", "Mac N Cheese")
your_order = Restaurant("Dunk", "Classic Donut")
his_order = Restaurant("Pizza Hut", "Extra Cheese Pizza")
our_order = Restaurant("Japanese Restaurant", "Sushi")

print(f"Restaurant of my choice is: {my_order.first}")
print(f"My order is: {my_order.second}")
my_order.describe_restaurant()

print(f"\nRestaurant of your choice is: {your_order.first}")
print(f"your order is: {your_order.second}")
your_order.describe_restaurant()

print(f"\nRestaurant of his choice is: {my_order.first}")
print(f"my order is: {my_order.second}")
my_order.describe_restaurant()
my_order.open_restaurant()

print(f"\nRestaurant of his choice is: {his_order.first}")
print(f"his order is: {his_order.second}")
his_order.describe_restaurant()
his_order.open_restaurant()

print(f"\nRestaurant of his choice is: {our_order.first}")
print(f"our order is: {our_order.second}")
our_order.describe_restaurant()
our_order.open_restaurant()
our_order.set_number_served(35)
print(f"Number of customers served: {our_order.number_served}")
our_order.increment_number_served(40)
print(f"Number of customers served: {our_order.number_served}")