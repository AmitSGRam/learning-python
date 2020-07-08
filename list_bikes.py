#Learning how to use lists

motorcycles=['kawasaki','honda','ducati','suzuki']
print(motorcycles)

#printing a desired item from the list(remember, list starts with 0 and NOT 1)
fav_bike=f"My favorite motorcycle is {motorcycles[0].upper()}"
print(fav_bike)
#using [-x] will use the last item from the list
print(motorcycles[-1].title())

#we can replace an item in the list by (look below)
motorcycles[0]='bmw'
print(motorcycles)

#adding items to the list
motorcycles.append('ducati')
print(motorcycles)

#adding item to the desired position in the list
motorcycles.insert(3,'yamaha')
print(motorcycles)

#removing a desired item from the list
del motorcycles[-3]
print(motorcycles)

#removing an item using pop(), it pops the last item on the list
removed=motorcycles.pop()
print(removed)

#remove an item and use it later
too_expensive=motorcycles[0]
print(f"\nI won't be able to buy {too_expensive.upper()} motorcycle because it is way too expensive for me")