import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create an employee data for use in all test methods.
        """
        first_name = 'Amit'
        last_name = 'Suresh'
        annual_salary = 40000
        self.my_employee = Employee(first_name, last_name, annual_salary)
    
    def test_give_default_raise(self):
        """Test that default raise is given to an employee."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 45000)

    def test_give_custom_raise(self):
        """Test that custom raise is given to an employee."""
        self.my_employee.give_raise(50000)
        self.assertEqual(self.my_employee.annual_salary, 90000)

if __name__ == '__main__':
    unittest.main()