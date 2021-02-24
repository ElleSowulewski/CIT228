import json

glossary = {
    "Assignment": "Giving a value to a variable",
    "Conditional Statement": "Statement that contains an 'if' or 'if/else'",
    "Debugging": "The process of finding and removing programming errors",
    "Dictionary": "A mutable associative array of key and value pairs",
    "Exception": "Means of breaking out of the normal flow of control of a code block in order to handle errors or other exceptional conditions",
    "Expression": "Python code that produces a value",
    "Import": "Used to import modules whose functions or variables can be used in the current program",
    "Indentation": "Python uses white-space indentation, rather than curly braces or keywords, to delimit blocks",
    "String": "Can include numbers, letters, and various symbols and be enclosed by either double or single quotes",
    "Variable": "Placeholder for texts and numbers. The equal sign (=) is used to assign values to variables",
}

def write(glossary):
    filename = 'Chapter10/glossary.json'
    with open(filename, "w+") as write_file:
        json.dump(glossary, write_file)
        print("Completed.")
        print()

def append(new_item):
    filename="Chapter10/glossary.json"
    with open(filename, "r+") as add_file:
        glossary = json.load(add_file)
        glossary.update(new_item)
        add_file.seek(0)
        json.dump(glossary, add_file, indent=0, sort_keys=True)
        print("Glossary submission has been added to ", filename)
        print()

def read():
    filename="Chapter10/glossary.json"
    try:
        with open(filename) as read_file:
            glossary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.") 
    else: 
        for key, value in glossary.items():
            print(key + " -")
            print("\t" + "Definition: " + value)
            print()

def menu():
    loop = True
    while loop == True:
        print("[a] Write current glossary to JSON file")
        print("[b] Add to JSON file")
        print("[c] Read JSON file")
        print("[q] Quit")
        print()
        choice = input("Please enter a menu choice: ").lower()
        print()
        if choice == "a":
            write(glossary)
        elif choice == "b":
            new_key = input("What vocab word would you like to add to the glossary? :")
            new_value = input("Please enter the definition of " + new_key + " ")
            new_dictionary_entry={new_key:new_value}
            append(new_dictionary_entry)
        elif choice == "c":
            read()
        elif choice == "q":
            loop = False
            break
        else:
            print(f"{choice} is not a valid response, please try again.")
            print()

menu()
