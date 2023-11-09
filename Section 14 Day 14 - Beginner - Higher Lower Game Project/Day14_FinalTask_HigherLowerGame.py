from replit import clear
from random import choice
from art import logo, vs
from game_data import data

end_game = False
score = 0
B = choice(data)

while end_game == False:
    A = B
    B = choice(data)
    if A == B:
        B = choice(data)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user_choice == 'A':
        if A['follower_count'] > B['follower_count']:
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            end_game = True
    elif user_choice == 'B':
        if B['follower_count'] > A['follower_count']:
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            end_game = True