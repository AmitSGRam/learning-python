from IceCreamStand import IceCreamStand as ice_cls


other_order = ice_cls("Chinese Restaurant", "Camel",'chocolate',1,'yes')


print("\n")

print(f"\nRestaurant of his choice is: {other_order.first}")
print(f"other order is: {other_order.second}")
other_order.describe_restaurant()
other_order.open_restaurant()
other_order.set_number_served(35)
other_order.describe_restaurant()
print(f"Number of customers served: {other_order.number_served}")
other_order.increment_number_served(40)
print(f"Number of customers served: {other_order.number_served}")
other_order.order_att.get_flavors()
other_order.order_att.get_icecream_or_not()
other_order.order_att.get_number_of_orders()