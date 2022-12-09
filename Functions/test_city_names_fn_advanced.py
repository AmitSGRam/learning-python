import unittest
from city_names_fn import city_country

class CityNamesTestCase(unittest.TestCase):
    def test_sum_string_of_ints(self):
        result = city_country('Rio de Janeiro', 'Brazil', '214000000')
        self.assertEqual(result, 'Rio de Janeiro, Brazil - 214,000,000')

if __name__ == '__main__':
    unittest.main()
    