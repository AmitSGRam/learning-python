# try:									#using try-except block
# 	print(5/0)
# except ZeroDivisionError:
# 	print("You can't divide by zero!")


# print("give me two numbers to divide")	#using else block
# print("Enter q to quit")

# while True:							#using exceptions to prevent crashes
# 	first_number=input("\nFirst Number:")
# 	if first_number=='q':
# 		break
# 	second_number=input("\nSecond Number:")
# 	if second_number=="q":
# 		break
# 	answer=int(first_number)/int(second_number)
# 	print(answer)


print("give me two numbers to divide")	#using else block
print("Enter q to quit")

while True:
	first_number=input("\nFirst Number:")
	if first_number=='q':
		break
	second_number=input("\nSecond Number:")
	if second_number=="q":
		break
	try:
		answer=int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)