from cars_c2 import Car, ElectricCar		#importing multiple classes from a module

my_beetle=Car('volkswagen','beetle',2019)
print(my_beetle.describe_car())
print("\n")
my_tesla=ElectricCar('tesla','roadster','2019')
print(my_tesla.describe_car())