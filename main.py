import random
numberChoice = 0
attemptCount = 1
maxAttempts = 5
randInt = random.randrange(0, 100)
print(randInt)
print("I'm thinking of number between 0 and 100, you must guess it etc, etc, etc.")


print("What difficulty do you want? \n 1. Easy (10 Chances) \n 2. Medium (5 chances) \n 3. Hard (3 Chances)")
Difficulty = int(input("Enter your choice: "))
if Difficulty == 1:
    maxAttempts = 10
elif Difficulty == 2:
    maxAttempts = 5
elif Difficulty == 3:
    maxAttempts = 3


while numberChoice != randInt and attemptCount <= maxAttempts:
    numberChoice = int(input("What number do you think it is? "))
    if numberChoice == randInt:
        print("Yay You Got it in ", attemptCount, " attempts.")
    elif numberChoice > randInt:
        print("The Number is less than ", numberChoice)
        attemptCount = attemptCount + 1
    elif numberChoice < randInt:
        print("The number is more than ", numberChoice)
        attemptCount = attemptCount + 1
if attemptCount > maxAttempts:
    print("Too many attempts, you lose.")