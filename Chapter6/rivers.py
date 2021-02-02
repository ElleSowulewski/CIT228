rivers = {
    "Nile": "Egypt",
    "Mississippi": "United States",
    "Yellow": "China",
}

print("-----------------------Rivers & Countries-----------------------")
for key, value in rivers.items():
    print(f"The {key} River runs through the country {value}")
print("----------------------------------------------------------------") 
print()
print("-----------------------------Rivers-----------------------------")
for key, value in rivers.items():
    print(f"{key} River")
print("----------------------------------------------------------------") 
print()
print("----------------------------Countries---------------------------")
for key, value in rivers.items():
    print(value)
print("----------------------------------------------------------------") 
print()

