class Employee:
    """Collect details of an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store First Name, Last Name, Annual Salary of an employee."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self,salary_raise=5000):
        """Add $5,000 to annual salary but also accept different amount."""
        self.annual_salary += salary_raise

    #def show_salary(self):
    #    print(f"Employee {self.first_name} {self.last_name} makes {self.annual_salary}")

#Amit = Employee('Amit', 'Suresh', 50000)
#Amit.give_raise()
#Amit.show_salary()