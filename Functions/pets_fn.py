def describe_pet(animal_type, pet_name='dike'):
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}\'s name is {pet_name.title()}")

describe_pet('dog', 'spike')
describe_pet('cat', 'tom')
describe_pet(pet_name='jerry', animal_type='rat')
describe_pet(animal_type='bunny', pet_name='bugs bunny')
describe_pet(animal_type='dog')