from random import randint

class Die:
    """Represent a die which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides
        self.roll_result = None
        
    def roll_die(self,sides):
        """Return a number between 1 and the number of sides."""
        if isinstance(self.sides, int) and self.sides > 0:
            self.roll_result = randint(1, self.sides)
            #print(f"The die is rolled: {self.roll_result}")
            return self.roll_result
        else:
            print(f"Please provide a valid input for the sides of a die.")

class Roll():
    """Represent number of times you want to roll a die."""

    def __init__(self, sides=6, roll_count=1):
        """Initialize the roll"""
        self.sides = sides
        self.roll_count = roll_count
        self.result_list = []

    def roll_times(self):
        if isinstance(self.roll_count, int) and self.roll_count > 0:
            for roll_num in range(self.roll_count):
                self.result_list.append(Die.roll_die(self,self.sides))
                #print(self.roll_die(sides))
                #print(self.die_att.roll_die())
            print(f"\n{self.roll_count} rolls of a {self.sides}-sided die:")
            print(f"\t{self.result_list}")


first = Roll(10, 10)
first.roll_times()

second = Roll(20, 10)
second.roll_times()
