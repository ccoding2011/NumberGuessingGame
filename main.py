import random

import json


highscore = 0
numberChoice = 0
attemptCount = 0
maxAttempts = 5

print()
IwantToPlay = True

while IwantToPlay == True:
    with open("score.json", "r") as f:
        jsonData = json.load(f)
        print(jsonData)
        highscore = jsonData["highscore"]

    randInt = random.randrange(0, 100)
    numberChoice = 0
    attemptCount = 1
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
            print("Yay You Got it in", attemptCount, "attempt(s).")
            if attemptCount > highscore or highscore == 0:
                highscore = attemptCount
                print("New Highscore! ", highscore)
                jsonData["highscore"] = highscore
                with open("score.json", "w") as f:
                    json.dump(jsonData, f, indent=4)
        elif numberChoice > randInt:
            print("The Number is less than ", numberChoice)
            attemptCount = attemptCount + 1
        elif numberChoice < randInt:
            print("The number is more than ", numberChoice)
            attemptCount = attemptCount + 1
    if attemptCount > maxAttempts:
        print("Too many attempts, you lose.")
    print("Would you like to play again? (y/n)")
    if input(": ") == 'y':
        IwantToPlay = True
        print("Restarting...")
    else:
        IwantToPlay = False
        print("Exiting Game.")
