class Dog:
	def __init__(self,name,age):
		self.name=name.title()
		self.age=age
	def sit(self):
		print(f"{self.name} is now sitting")
	def roll_over(self):
		print(f"{self.name} is now rolling over")
my_dog=Dog('timmy',6)
your_dog=Dog('jimmy',9)
print(f"\nMy dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()