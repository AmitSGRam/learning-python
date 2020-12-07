import cars_c2		#importing an entire module	

my_beetle=cars_c2.Car('volkswagen','beetle',2019)
print(my_beetle.describe_car())
print("\n")
my_tesla=cars_c2.ElectricCar('tesla','roadster','2019')
print(my_tesla.describe_car())

#importing all classes from a module- from module_name ipmort *