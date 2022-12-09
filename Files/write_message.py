filename = 'Files/programming.txt'

with open(filename, 'w') as file_object:
    file_object.write(str(1))
    file_object.write('. I love programming.\n')
    file_object.write(str(2))
    file_object.write('. I love creating new games.\n')