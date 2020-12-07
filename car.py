class Car:

	def __init__(self,name,model,year):
		self.n1=name
		self.m1=model
		self.y1=year
		self.odometer_reading=0	#setting a default value for an attribute

	def describe_car(self):
		full_name=f"{self.n1} {self.m1} {self.y1}"
		return full_name.title()

	def rd_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self,mileage):		#modifying an attribute's value through a method
		if mileage>=self.odometer_reading:
			self.odometer_reading=mileage
		else:
			print("You can't roll back an odometer!!!!!!!")
