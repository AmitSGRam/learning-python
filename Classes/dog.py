class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.first_attribute = name
        self.second_attribute = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.first_attribute} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.first_attribute} rolled over!")

my_doggo = Dog('jimmy',7)
your_doggo = Dog('spike', 6)

print(f"My dog\'s name is {my_doggo.first_attribute}")
print(f"My dog is {my_doggo.second_attribute} year\'s old")
my_doggo.sit()
my_doggo.roll_over()

print(f"Your dog\'s name is {your_doggo.first_attribute}")
print(f"Your dog is {your_doggo.second_attribute} year\'s old")
your_doggo.sit()
your_doggo.roll_over()