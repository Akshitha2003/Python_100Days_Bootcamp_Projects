#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

import random
original_number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
no_of_attempts = 0
if difficulty == 'easy':
    no_of_attempts = 10
elif difficulty == 'hard':
    no_of_attempts = 5

end_game = False

def make_predictions(original_number):
    print(f"You have {no_of_attempts} attempts remaining to guess the number.")
    prediction_number = int(input("Make a guess: "))
    if original_number > prediction_number:
        print("Too low.")
    elif original_number < prediction_number:
        print("Too high.")
    elif original_number == prediction_number:
        print(f"You got it! The answer was {original_number}.")
        global end_game
        end_game = True

while end_game == False and no_of_attempts != 0:
    make_predictions(original_number=original_number)
    if end_game == False:
        no_of_attempts -= 1
        if no_of_attempts != 0:
            print("Guess again.")

if no_of_attempts == 0:
    print("You've run out of guesses, you lose.")