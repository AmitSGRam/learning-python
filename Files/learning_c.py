file_name = 'Files/learning_python.txt'

with open(file_name) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip().replace('Python', 'C'))