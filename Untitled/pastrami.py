sandwich_orders = []
finished_orders = []
flag1 = True

while flag1:
    my_orders = input("\nPlease Enter your orders, one at a time. If that is all, please enter \"I'm done.\" ")
    if my_orders == "I'm done.":
        flag1 = False
    else:
        sandwich_orders.append(my_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    if 'pastrami' in sandwich_orders:
        print(f"\nSorry, we are out of pastrami.")

while sandwich_orders:
        #add_orders = sandwich_orders.pop()
        #finished_orders.append(add_orders)
        finished_orders.append(sandwich_orders.pop())
        print(finished_orders)

print(f"\nThe finished orders are: {finished_orders}")

print(len(sandwich_orders))
print(len(finished_orders))

for initial_orders in sandwich_orders:
    print(f"\n My initial orders are: {initial_orders.title()}")

print(f"\nMy finished orders are: ") 
for finished_order in finished_orders:
    print(f"\t\t\t{finished_order.title()}")

print(len(sandwich_orders))
print(len(finished_orders))