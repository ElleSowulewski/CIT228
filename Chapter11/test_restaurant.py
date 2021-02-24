from restaurant import Restaurant
import unittest

class TestRestaurant(unittest.TestCase):

    def setUp(self):
        restaurant_name="Cheezy's Pizza"
        cuisine_type="Pizza"
        number_served=12000
        self.restaurant = Restaurant(restaurant_name, cuisine_type, number_served)

    def test_set_number_served(self):
        self.restaurant.set_number_served()
        self.assertEqual(self.restaurant.number_served,"12001")

    def test_increment_number_served(self):
        self.restaurant.increment_number_served()
        self.assertEqual(self.restaurant.number_served, 12001)

if __name__ == '__main__':
    unittest.main()