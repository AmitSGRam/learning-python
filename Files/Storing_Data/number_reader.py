import json

filename = 'Files/Storing_Data/numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)