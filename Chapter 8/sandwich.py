items = []

def sandwich_items(num):
    while num > 0:
        item = input("Pleas enter the item you would like to add to your sandwich: ")
        items.append(item)
        num-=1
    print()
    print("The items you added to your pizza are:")
    for i in items:
        print(i)

num = int(input("How many items would you like on your sandwich? "))
sandwich_items(num)