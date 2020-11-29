class Robot:
	def __init__(self, Name,Color,Weight): #we can create a custom constructor by using __init__
		self.name = Name
		self.color = Color
		self.weight = Weight
	def introduce_self(self):
		print("My name is " + self.name) #this (for self) in Java
r1 = Robot("Tom","red",30)
r2 = Robot("Jerry","blue",40)

class Person:
	def __init__(self,n,p,i): #we can add another argument r and say self.robot_owned = r
		self.name = n
		self.personality = p
		self.is_sitting = i

	def sit_down(self):
		self.is_sitting = True

	def stand_up(self):
		self.is_sitting = False

p1 = Person("Alice", "aggressive",False)
p2 = Person("Becky","talkative",True)

#p1 owns r2
p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self() #Jerry is the robot owned by Alice
p2.robot_owned.introduce_self() #Tom is the robot owned by Becky