class Restaurant: 
    "The class containing the attributes of a restaurant"

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a restaurant serving {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open!")

my_restaurant = Restaurant("Cheezy's", "Fast")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print()
your_restaurant = Restaurant("Pasta Time", "Italian")
your_restaurant.describe_restaurant()
print()
their_restaurant = Restaurant("Mike's Diner", "Greek")
their_restaurant.describe_restaurant()