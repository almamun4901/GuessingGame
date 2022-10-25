import random

def guessGame():
    counter = 0
    computerGuess = int(random.randint(1, 100))

    while True:
        userInput = int(input("Enter your guess: "))
        counter = counter + 1

        if userInput > computerGuess:
            print("Your guess is higher than computer number")
            print("You have tried",counter, "times")
        elif userInput < computerGuess:
            print("Your guess is lower than computer number")
            print("You have tried",counter, "times")
        else:
            print("Your guess is correct")
            print("You have tried",counter, "times")
            break

guessGame()
