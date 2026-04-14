# This is a guessing game where the player need to guess a 
# number between 1 to 10 which the computer guesses.
import random

number_tries = 0
number_to_guess = random.randint(1, 10)
current_guess = None

while number_tries < 5:
    print("Input:")

    try:
        current_guess = int(input("Guess the number (1-10): "))
    except:
        print("Please input a number!!!\n")
        continue

    if current_guess == number_to_guess:
        print("Output:")
        print("Correct! You guessed it.")
        break
    else:
        if current_guess > number_to_guess:
            print("Too high!\n")
        else:
            print("Too low!\n")
    number_tries = number_tries + 1

if number_tries == 5:
    print("Sorry you lose!!!")
    print("The number to guess is", number_to_guess)