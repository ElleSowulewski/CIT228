print("-------------------Printing Lists-------------------")
birds = ["quail", "hawk", "pigeon", "falcon", "robin", "sparrow"]
print(f"Here is a list of birds: {birds}")
print(f"Here is the first and last bird in the list: {birds[0]} {birds[-1]}")
print("-------------------Altering Lists-------------------")
birds[2] = "parrot"
print(f"Here I changed the third bird in the list: {birds}")
birds.append("duck")
print("-------------------Adding to Lists-------------------")
print(f"Here I appended an item: {birds}")
birds.insert(3, "budgie")
print(f"Here I inserted an item: {birds}")
del birds[-1]
print("-------------------Deleting from Lists-------------------")
print(f"Here I deleted the last item: {birds}")
poppedBird = birds.pop(3)
print(f"Here I popped an item: {birds}")
print(f"Here is the item I popped: {poppedBird}")
birds.remove("robin")
print(f"Here I removed robin: {birds}")
print("-------------------Sorting Lists-------------------")
print(f"Here I temporarily sorted: {sorted(birds)}")
print(f"Here it is in original order again: {birds}")
birds.sort()
print(f"Here I permanantly sorted: {birds}")
birds.reverse()
print(f"Here I reverse sorted: {birds}")
print("-------------------Lengths of Lists-------------------")
print(f"Here is the length of the list: {len(birds)}")