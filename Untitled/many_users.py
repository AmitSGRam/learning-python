users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
    },
    'mcurie' : {
        'first' : 'marie',
        "last" : "curie",
        'location' : 'paris',
    }
}

for username, keyy in users.items():
    print(f'\nUsername: {username}')
    full_name = f"{keyy['first']} {keyy['last']}"
    location = f"{keyy['location']}"
    print(f'\tFull Name: {full_name.title()}')
    print(f"\tLocation: {location.title()}")
print('~~~~~~~~~~~~~~~~')
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")