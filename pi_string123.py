file='pi_digits.txt'
with open(file) as file_obj:
	l=file_obj.readlines()
pi_string=''
for l1 in l:
	pi_string += l1.strip()
print(pi_string)
print(len(pi_string))

birthday=input('enter your birthday mmddyy :')
if birthday in pi_string:
	print('Your birthday appears in the first million digits of pi')
else:
	print("Your birthday does not appear in the first million digits of pi")