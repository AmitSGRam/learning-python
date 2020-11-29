# age=input("How old are you?")
# age #when run this will print the age because python interprets it as a string


# age=input("How old are you?")
# age>=18 #Traceback error as the string that we assign cannot be compared to the numerical value 18

age = input("How old are you?")
age = int(age)
if age >=18:
	print(bool(age))