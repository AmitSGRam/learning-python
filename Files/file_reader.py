#file_path = 'F:\lin\python\Files\pi_digits.txt'
file_path = 'Files/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())