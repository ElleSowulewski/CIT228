menu = {
    "Foods": ["Burger", "Fry", "Pizza", "Nachos"],
    "Drinks": ["Soda", "Tea", "Coffee", "Water"],
    "Desserts": ["Ice Cream", "Cake", "Milkshake", "Pie"]
}
for key, value in menu.items():
    print(f"The {key.title()} on the menu:")
    for v in value:
        print("\t\t\t\t",v)