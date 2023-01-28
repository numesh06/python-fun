# my code 1
import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess == random_number:
            print(f"Yay, congrats. You have guessed the number {guess} correctly!!")
            break
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        elif guess < random_number:
            print("Sorry, guess again. Too low.")
            continue
        # else:
        #     print("Sorry, guess again.")
        #     continue
guess(10)

# OR
# my code 2

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number: 
        guess = int(input(f"Guess a number bwetween 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yay, congrats.You have guessed the number {random_number} correctly.")    





