def get_formatted_name(first_name, last_name):
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

while True:
    print("\nPlease tell me your name:")
    print("\nenter 'q' at any time to quit")
    f_name = input("First Name\t")
    if f_name == 'q':
        break
    l_name = input("Last Name\t")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")