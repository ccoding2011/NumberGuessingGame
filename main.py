#Imports
import random
import json

#Variable Declares
highscore = {
    "Highscore": 0
    }
numberChoice = 0
attemptCount = 0
maxAttempts = 5
Difficulty = 1
IwantToPlay = True

#Convert attemptCount and Difficulty to score using formula
def attemptToScore():
    score = 100 - attemptCount * 10 + Difficulty + 11 - (10 - Difficulty * 2)
    return score 


#Main Loop
while IwantToPlay == True:
    #Open score.json file and read highscore
    with open("score.json", "r") as f:
        jsonData = json.load(f)
        print(jsonData)
        highscore = jsonData["highscore"]

    #Generate Rand int and reset vars
    randInt = random.randrange(0, 100)
    numberChoice = 0
    attemptCount = 1
    print(randInt) #DEBUG
    #Game Hello Message & Difficulty selection
    print("I'm thinking of number between 0 and 100, you must guess it etc, etc, etc.")
    print("What difficulty do you want? \n 1. Easy (10 Chances) \n 2. Medium (5 chances) \n 3. Hard (3 Chances)")

    Difficulty = int(input("Enter your choice: "))
    if Difficulty == 1:
        maxAttempts = 10
    elif Difficulty == 2:
        maxAttempts = 5
    elif Difficulty == 3:
        maxAttempts = 3

    #Number guessing loop
    while numberChoice != randInt and attemptCount <= maxAttempts: # Check if attempted too many times & if number is correct
        numberChoice = int(input("What number do you think it is? "))
        if numberChoice == randInt: # if number is correct
            print("Yay You Got it in", attemptCount, "attempt(s).")
            score = attemptToScore() #convert attempt to score
            print(score) #DEBUG
            if score > highscore or highscore == 0: # Check if score is a new highscore
                highscore = score
                print("New Highscore! ", highscore)
                jsonData["highscore"] = highscore
                with open("score.json", "w") as f: #Open json file and write highscore
                    json.dump(jsonData, f, indent=4)
        # If number is more than say so and vice versa and increment attempCount
        elif numberChoice > randInt: 
            print("The Number is less than ", numberChoice)
            attemptCount = attemptCount + 1
        elif numberChoice < randInt:
            print("The number is more than ", numberChoice)
            attemptCount = attemptCount + 1
    #Check if if attempted more than allowed
    if attemptCount > maxAttempts:
        print("Too many attempts, you lose.")
        print("The number was ", randInt)
    #Ask for replay
    print("Would you like to play again? (y/n)")
    if input(": ") == 'y':
        IwantToPlay = True
        print("Restarting...")
    else:
        IwantToPlay = False
        print("Exiting Game.")
