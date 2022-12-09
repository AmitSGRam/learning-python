import json

"""
    Promp for the user's favorite number.
    Store the number in a file.
    Read the stored number.
"""

def get_favorite_number():
    """Prompt for favorite number."""
    fav_number = input("Please enter your favorite number: ")
    return fav_number

def store_favorite_number():
    """Store the number in a file."""
    try:
        filename = 'Files/Storing_Data/favorite_number.json'
        fav_num = get_favorite_number()
        with open(filename, 'w') as f:
            json.dump(fav_num, f)
    except FileNotFoundError:
        return None
    else:
        print(f'Your favorite number {fav_num} has been stored in {filename.split("/")[2]}')

def read_stored_number():
    """Read the stored number."""
    try:
        filename = 'Files/Storing_Data/favorite_number.json'
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        #store_favorite_number()
        return None
    else:
        return fav_num
        #print(f"I know your favorite number! It's {fav_num}")

def favorite_number():
    fav_num = read_stored_number()
    if fav_num:
        print(f"I know your favorite number! It's {fav_num}")
    else:
        store_favorite_number()

favorite_number()