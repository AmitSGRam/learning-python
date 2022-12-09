def read_contents(filename):
    
    try:
        with open(filename, encoding='utf-8') as f:
            files = f.read()
            print(files)
    except FileNotFoundError:
        print('file doesn\'t exist')

filenames = ['Files/Exceptions/cats.txt', 'Files/Exceptions/dogs.txt']
for filename in filenames:
    print(f'\nReading file: {filename.split("/")[2]}')
    read_contents(filename)