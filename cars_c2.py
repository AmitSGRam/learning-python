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

class Battery:
	
	def __init__(self,battery_size=75):
		self.battery_size=battery_size
	
	def describe_battery(self):
		print(f"This car has a {self.battery_size} -KWh Battery.")
	
	def get_range(self):
		if self.battery_size==75:
			range=260
		elif self.battery_size==100:
			range=315

		print(f"This car can go about {range} miles on a full charge!")

class ElectricCar(Car):
	
	def __init__(self,name,model,year):
		super().__init__(name,model,year)
		self.battery=Battery()