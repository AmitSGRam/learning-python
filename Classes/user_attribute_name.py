import re

class User:
    """A class to store user's information and greet them."""

    def __init__(self, first_name, last_name, age):
        self.first_name1 = first_name
        self.last_name1 = last_name
        #self.username = "".join([first_name, last_name])
        names_comb = "".join([self.first_name1.lower(), self.last_name1.lower()])
        #joinnames = "".join([first_name.lower(), last_name.lower()])
        #print(f"{names_comb}")
        joinnames = re.sub(r"\s+", "", names_comb, flags=re.UNICODE)
        #joinnames = "".join([names_comb.replace(" ", "")])
        self.username = joinnames
        self.age = age

    def describe_user(self):
        print(f"\nUser Info:\n\tName:\t{self.first_name1} {self.last_name1}\n\tAge :\t{self.age}")
    
    def greet_user(self):
        #un = "".join(self.username.split())
        #print(f"\nHello, {un.lower()}")
        #print(f"\nHello, {self.username.lower()}")
        print(f"\nHello, {self.username}")

my_user = User("Amit", "S G Ram", 25)
cuz_user = User("Akshit", "Ragukumar", 24)
bro_user = User("Abijit", "S G Ram", 32)

print(f"My name is {my_user.first_name1.title()} {my_user.last_name1.title()}")
my_user.describe_user()
my_user.greet_user()

print(f"\nMy name is {bro_user.first_name1.title()} {bro_user.last_name1.title()}")
bro_user.describe_user()
bro_user.greet_user()

print(f"\nMy name is {cuz_user.first_name1.title()} {cuz_user.last_name1.title()}")
cuz_user.describe_user()
cuz_user.greet_user()