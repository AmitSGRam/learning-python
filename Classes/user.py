import re

class User:
    """A class to store user's information and greet them."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        #self.username = "".join([first_name, last_name])
        names_comb = "".join([first_name.lower(), last_name.lower()])
        #joinnames = "".join([first_name.lower(), last_name.lower()])
        #print(f"{names_comb}")
        joinnames = re.sub(r"\s+", "", names_comb, flags=re.UNICODE)
        #joinnames = "".join([names_comb.replace(" ", "")])
        self.username = joinnames
        self.age = age
        self.logic_attempts = 0

    def describe_user(self):
        print(f"\nUser Info:\n\tName:\t{self.first_name} {self.last_name}\n\tAge :\t{self.age}")
    
    def greet_user(self):
        #un = "".join(self.username.split())
        #print(f"\nHello, {un.lower()}")
        #print(f"\nHello, {self.username.lower()}")
        print(f"\nHello, {self.username}")

    def increment_login_attempts(self):
        #self.logic_attempts = self.logic_attempts + 1
        self.logic_attempts += 1

    def reset_log_attempts(self):
        self.logic_attempts = 0

my_user = User("Amit", "S G Ram", 25)
cuz_user = User("Akshit", "Ragukumar", 24)
bro_user = User("Abijit", "S G Ram", 32)

print(f"My name is {my_user.first_name.title()} {my_user.last_name.title()}")
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
print(f"Login attempts of my user is: {my_user.logic_attempts}")
my_user.reset_log_attempts()
print(f"Login attempts of my user is: {my_user.logic_attempts}")
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(f"Login attempts of my user is: {my_user.logic_attempts}")
my_user.reset_log_attempts()
print(f"Login attempts of my user is: {my_user.logic_attempts}")

print(f"\nMy name is {bro_user.first_name.title()} {bro_user.last_name.title()}")
bro_user.describe_user()
bro_user.greet_user()

print(f"\nMy name is {cuz_user.first_name.title()} {cuz_user.last_name.title()}")
cuz_user.describe_user()
cuz_user.greet_user()