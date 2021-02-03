sandwich_orders = ["tuna", "pastrami", "tuna", "pastrami", "egg", "ham", "italian", "turkey", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami.  :(")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == "pastrami":
        print("I am sorry, we are out of pastrami.")
    else:
        print(f"I made the {current_sandwich} sandwich!")
        finished_sandwiches.append(current_sandwich)