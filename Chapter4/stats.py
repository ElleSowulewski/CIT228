import random

num = list(range(random.randrange(10,100)))
print(num)

print("The largest number is: ", max(num))
print("The smallest number is: ", min(num))
print("The total of all the numbers is: ", sum(num))
print("The average number is: ", sum(num)/len(num))