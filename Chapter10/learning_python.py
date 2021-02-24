filename = "Chapter10/learning_python.txt"

with open(filename) as textFile:
    myText = textFile.read()

# From read()
print(myText)

# From for loop
with open(filename) as textFile:
    for line in textFile:
        print(line)

# From readlines() as list
with open(filename) as textFile:
    myText = textFile.readlines()

for line in myText:
    print(line)

#------------------------------------------
with open(filename) as textFile:
    for line in textFile:
        print(line.replace("Python", "C#"))

