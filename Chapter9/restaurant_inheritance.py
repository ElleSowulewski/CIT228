class Restaurant: 
    "The class containing the attributes of a restaurant"

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a restaurant serving {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open!")
    
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "mint chip", "butter pecan"]

    def display_flavors(self):
        print("Flavor list:")
        for i in self.flavors:
            print(i)

stand = IceCreamStand("Frosty", "Ice Cream Stand")
stand.display_flavors()