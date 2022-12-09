filename = 'Files/guest_book.txt'

with open(filename, 'r') as file_object:
    count = len(file_object.readlines())
    count += 1

with open(filename, 'a') as file_object:
    guest_name = input('Please enter your name. \nPlease enter \'quit\' to quit the program.')
    while True:
        if isinstance(guest_name, str):
            if guest_name.lower() == 'quit' or guest_name.startswith('/') or guest_name is None or guest_name.strip() == '': 
                break
            else:
                print('Greetings.')
                file_object.write(f'{count}. {guest_name} \n')
                break