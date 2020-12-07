from car import Car

from electric_car1 import ElectricCar as EC 		#using Aliases

my_beetle=Car('volkswagen','beetle',2019)
print(my_beetle.describe_car())

my_tesla=EC('tesla','roadster',2019)
print(my_tesla.describe_car())