import json

filename = 'Files/Storing_Data/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")