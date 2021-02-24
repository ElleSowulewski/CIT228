import random
import os
rooms = []
filename = "Chapter10/guests.txt"

if os.path.exists(filename):
    os.remove(filename)

name = input("Hello! Please enter your name [enter q to quit]:").title()
with open(filename, "w") as textFile:
    while name != "Q":
        number = random.randint(1, 50)
        while number in rooms:
            number = random.randint(1, 50)
        rooms.append(number)
        print(f"Welcome, {name}! You are in room {number}. Have a nice stay!")
        print()
        name += ", room #: " + str(number) + "\n"
        textFile.write(name)
        name = input("Hello! Please enter your name [enter q to quit]:").title()

print()
print("------------Room Assignment------------")
with open(filename) as textFile:
    for line in textFile:
        print(line)