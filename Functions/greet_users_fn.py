def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
usernames = ['hannah','stallion123', 'geralt']
greet_users(usernames)