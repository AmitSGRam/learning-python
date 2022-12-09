requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('adding extra cheese')
print('\nFinished making your first pizza')
print('\n~first~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
for toppings in requested_toppings:
    print(f'adding {toppings}')
print('\nFinished making your second pizza')
print('\n~second~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
for toppings in requested_toppings:
    if toppings == 'green peppers':
        print('Sorry, we are out of green peppers right now')
    else:
        print(f"Adding {toppings}")
print("\nFinished making your third pizza")
print('\n~third~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
requested_toppings = []

if requested_toppings:
    for toppings in requested_toppings:
        print(f"Adding {toppings}")
    print("Finished making your pizza")
else:
    print("Are you sure you want a plain pizza?")
print('\n~fourth~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
available_toppings = ['mushrooms', 'extra cheese', 'olives', 'green peppers', 'pepperoni', 'pineapple']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for req_topping in requested_toppings:
    if req_topping in available_toppings:
        print(f"Adding {req_topping}")
    else:
        print(f"Sorry, we don't have the {req_topping}")

print(f"\nFinished making your fourth pizza.")
print('\n~fifth~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
requested_toppings = ['mushrooms', 'extra cheese', 'olives']

if requested_toppings:
    for toppings in requested_toppings:
        print(f"Adding {toppings}")
    print("Finished making your pizza")
else:
    print("Are you sure you want a plain pizza?")