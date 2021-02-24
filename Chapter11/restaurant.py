class Restaurant: 
    "The class containing the attributes of a restaurant"

    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The {self.restaurant_name} is a restaurant serving {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open!")

    def set_number_served(self):
        self.number_served = input("Enter the number of customers served: ")
        print(f"The {self.restaurant_name} restaurant has served {self.number_served} customers!")

    def increment_number_served(self):
        self.number_served += int(input("Enter how many customers to add to served total: "))
        print(f"The {self.restaurant_name} restaurant has served {self.number_served} customers!")
