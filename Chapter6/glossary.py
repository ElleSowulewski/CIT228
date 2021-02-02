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

for key, value in glossary.items():
    print(key + " -")
    print("\t" + "Definition: " + value)
    print()