class Dog:
	def __init__(self,name,age):
		self.n1=name.title()
		self.a1=age
	def sit(self):
		print(f"{self.n1} is now sitting")
	def roll_over(self):
		print(f"{self.n1} is now rolling over")
my_dog=Dog('timmy',6)
your_dog=Dog('jimmy',9)
print(f"\nMy dog's name is {my_dog.n1}")
print(f"My dog is {my_dog.a1} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.n1}")
print(f"Your dog is {your_dog.a1} years old")
your_dog.sit()