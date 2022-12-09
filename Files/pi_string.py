#file_path = 'F:\lin\python\Files\pi_digits.txt'
file_path = 'Files/pi_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#filename = 'F:\lin\python\Files\pi_million_digits.txt'
filename = 'Files/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print(f"{pi_string[:52]}...")
print(len(pi_string))