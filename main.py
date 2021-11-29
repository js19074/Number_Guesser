#Number Guesser - Version 2
#29 Nov 2021
#Jasnoor

import random

#Target variable to store a random target number for the user to guess
target = random.randint(1, 100)

#Controls whether while loop runs. Repeat until user guesses correct number
run_loop = True

while run_loop:

    #Guess variable to store the user's guess number
    guess = int(input("Please guess the number (1-100): "))

    #Repeats until user inputs number between 1-100
    while not(guess >= 1 and guess <=100):
        guess = int(input("That is not a valid number. Please guess between 1 and 100: "))
    
    if guess < target:  #Checking whether the user's guess is less than the target
        print("Your guess was too low")
    elif guess > target:  #Checking whether the user's guess is greater than the target
        print("Your guess was too high")
    elif guess == target: #Check for correct guess
        #Stop repeating loop
        run_loop = False

    

#When the user has guessed the correct number
print("Congratulations! You got the number")





