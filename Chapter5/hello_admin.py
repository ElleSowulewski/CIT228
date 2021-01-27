usernames = ["admin", "Elle", "guest03", "Connor"]
if usernames:
    for login in usernames:
        if login == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {login},  thank you for logging in again.")
else:
    print("We need to find some users!")