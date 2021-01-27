current_users = ["admin", "Elle", "guest03", "Connor", "Nanners"]
new_users = ["Charles", "Nanners", "guest03", "Bean", "Grace"]

current_users_l=[]
for user in current_users:
    current_users_l.append(user.lower())

new_users_l=[]
for user in new_users:
    new_users_l.append(user.lower())

for names in new_users_l:
    if names in current_users_l:
        print(f"{names} has already been taken as a username. Please try a new one.")
    else:
        print("Username is available!")