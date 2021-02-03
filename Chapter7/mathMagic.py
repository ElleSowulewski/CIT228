import random
counter = 0
numberCorrect = 0
while counter < 10:
    randNum1 = random.randrange(1,1000)
    randNum2 = random.randrange(1,1000)
    correctAnswer = int(randNum1 + randNum2)
    yourAnswer = int(input(f"What is the answer of: {randNum1} + {randNum2}? "))
    if correctAnswer==yourAnswer:
        print("Great job!")
        print()
        numberCorrect+=1
    else:
        print(f"Oops, the correct answer is {correctAnswer}")
        print()
    counter+=1

print(f"You answered {numberCorrect} questions correctly!")
print("Thanks for playing!")