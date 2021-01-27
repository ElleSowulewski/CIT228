print("--------------Original List----------------")
farm = ["cow", "pig", "chicken", "sheep", "horse", "goat"]
for animal in farm:
    print(animal)
print("-----------------New List------------------")
newfarm = farm[:]
newfarm.append("llama")
newfarm.append("goose")
newfarm.append("quail")
newfarm.append("cat")
for animal in newfarm:
    print(animal)
print("-------------------4-10--------------------")
print(f"The first three items in the list are: {newfarm[0:3]}")
print(f"The four middle items in the list are: {newfarm[3:7]}")
print(f"The last three items in the list are: {newfarm[7:10]}")