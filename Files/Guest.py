guest_user = input('Please enter your name.')

filename = 'Files/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(guest_user)