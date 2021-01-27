print("-------------------------Chapter 4 Lab 1-------------------------")
foods = ["steak", "onions", "ice cream", "chicken noodle soup", "mac & cheese", "calamari"]
numbers = [8, 15, 24, 30, 64, 100]
movies = ["Forrest Gump", "Jurassic Park", "Happy Feet"]
combo = [foods[0], foods[1], numbers[2], numbers[3], movies[0], movies[1]]

print("       Favorite Food       ")
print("============================")
for food in foods:
    print(f"{food}")
print("============================")

print("      Favorite Numbers       ")
print("============================")
for nums in numbers:
    print(f"{nums}")
print("============================")

print("      Favorite Movies       ")
print("============================")
for movie in movies:
    print(f"{movie}")
print("============================")

print("         Combo List       ")
print("============================")
for item in combo:
    print(f"{item}")
print("============================")