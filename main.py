#Number Guesser - Version 1
#29 Nov 2021
#Jasnoor

import random

#Target variable to store a random target number for the user to guess
target = random.randint(1, 100)
#Guess variable to store the user's guess number
guess = int(input("Please guess the number: "))


if guess == target:   #Checking whether the user's guess is the same as the target
    print("Congratulations! You got the number")
elif guess < target:  #Checking whether the user's guess is less than the target
    print("Your guess was too low")
elif guess > target:  #Checking whether the user's guess is greater than the target
    print("Your guess was too high")
else:                 #In case something goes wrong - shouldn't actually run
    print("Something went wrong")



