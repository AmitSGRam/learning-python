from user import User as user_class

class Admin(user_class):

    def __init__(self, first_name, last_name, age, privileges=None):
        super().__init__(first_name, last_name, age)
        self.privilege_att = Privileges(privileges)

class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges and isinstance(self.privileges, list):
            print(f"\nThis user has the following set of privileges:")
            for privilege in self.privileges:
                print(f"\t{privilege}.")
        elif self.privileges and isinstance(self.privileges, str):
            print(f"\nThis user has {self.privileges} privilege.")
        else:
            print(f"This user has no privileges.")
    

admin_user = Admin('Amit', 'S G Ram', 24)
admin_user.describe_user()
admin_privileges = [
    'can add post', 
    'can delete post', 
    'can ban user'
    ]
admin_user.privilege_att = Privileges(admin_privileges)
admin_user.greet_user()
admin_user.privilege_att.show_privileges()