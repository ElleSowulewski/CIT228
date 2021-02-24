from city_functions import city_string
import unittest

class test_city_country(unittest.TestCase):

    def test_country_city(self):
        formatted_city = city_string('Santiago', 'Chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')   

    def test_country_city_population(self):
        formatted_city = city_string('Santiago', 'Chile', "500,000")
        self.assertEqual(formatted_city, 'Santiago, Chile = population 500,000')

if __name__ == '__main__':
    unittest.main()     

