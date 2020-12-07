from cars_c2 import ElectricCar

my_tesla=ElectricCar('tesla','model s',2019)

print(my_tesla.describe_car())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()