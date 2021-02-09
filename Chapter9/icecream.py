from restaurant import Restaurant
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "mint chip", "butter pecan"]

    def display_flavors(self):
        print("Flavor list:")
        for i in self.flavors:
            print(i)