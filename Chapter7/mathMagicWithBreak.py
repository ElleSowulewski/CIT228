import random
counter = 0
numberCorrect = 0
numberIncorrect = 0
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
        numberIncorrect+=1
    counter+=1
    if numberIncorrect > 5:
        print("You should seek help from a tutor")
        break

print(f"You answered {numberCorrect} questions correctly!")
print("Thanks for playing!")