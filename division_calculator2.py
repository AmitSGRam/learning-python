print("give me two numbers to divide")	#using else block
print("Enter q to quit")

while True:							#using exceptions to prevent crashes
	first_number=input("\nFirst Number:")
	if first_number=='q':
		break
	second_number=input("\nSecond Number:")
	if second_number=="q":
		break
	answer=int(first_number)/int(second_number)
	print(answer)