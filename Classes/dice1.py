from random import randint

class Die:
    """Represent a die which can be rolled."""

    def __init__(self, sides=6, roll_count=1):
        """Initialize the die."""
        self.sides = sides
        self.roll_result = None
        self.roll_count = roll_count
        self.result_list = []

    def roll_die(self,sides=5):
        """Return a number between 1 and the number of sides."""
        self.roll_result = randint(1, sides)
        #print(f"The die is rolled: {self.roll_result}")
        return self.roll_result

    def roll_times(self,sides=2):
        #if self.roll_count is not None and self.roll_count > 0:
            for roll_num in range(self.roll_count):
                #self.result_list.append(Die.roll_die(self.sides))
                self.result_list.append(self.roll_die(self.sides))
                #print(self.roll_die(sides))
            print(f"\n{self.roll_count} rolls of a {self.sides}-sided die:")
            print(f"\t{self.result_list}")
            #print(f"result:{self.result_list}")



#first = Roll()
#first.roll_times()
#print(f"The die is rolled: {first.die_att.roll_die()}")
#Roll.roll_times(10)
#first.roll_die()
first = Die(10, 10)
first.roll_times()

second = Die(20,10)
#print(second.roll_die())
second.roll_times()

#second = Die(20)
#second.roll_die()

