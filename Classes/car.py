class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odomoter_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odomoter_reading:
            self.odomoter_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odomoter_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")

    def update_battery(self):
        """Check the battery size and set the capacity to 100"""
        if self.battery_size != 100:
            self.battery_size = 100
            print(f"The battery capacity has been upgraded to {self.battery_size}")
        elif self.battery_size == 100:
            print(f"The battery capacity is already {self.battery_size}")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, batt_size):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        #self.battery_att = Battery(100)
        self.battery_att = Battery(batt_size)

my_car = Car('Tesla', 'Model 3', 2021)
print(my_car.get_descriptive_name())
my_car.read_odometer()

print('\n')

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odomoter_reading = 200
my_new_car.read_odometer()

print('\n')
his_car = Car('ferrari', '488 GT3 EVO', 2020)
print(his_car.get_descriptive_name())
his_car.update_odometer(3000)
his_car.read_odometer()

print('\n')
his_new_car = Car('ferrari', '488 GT3 EVO', 2020)
print(his_new_car.get_descriptive_name())
his_new_car.odomoter_reading = 200
his_new_car.update_odometer(20)
his_new_car.read_odometer()

print("\n")
our_car = Car('Ferrari', '296 gtb', 2021)
print(our_car.get_descriptive_name())
our_car.odomoter_reading = 1400
our_car.read_odometer()
our_car.increment_odometer(299)
our_car.read_odometer()
print('\n')

my_tesla = ElectricCar('tesla', 'model s', 2022, 75)
print(my_tesla.get_descriptive_name())
#my_tesla.describe_battery()
my_tesla.battery_att.describe_battery()
my_tesla.battery_att.get_range()
my_tesla.battery_att.update_battery()
my_tesla.battery_att.get_range()