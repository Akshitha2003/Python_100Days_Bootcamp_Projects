############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

import random
from replit import clear
from art import logo

while choice == "y":
    clear()
    print(logo)
    
    #Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
    #11 is the Ace.
    #cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    def deal_card():
        """Returns a random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)
    
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    #user_cards = []
    #computer_cards = []
    
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
    print("    Computer's first card: ", computer_cards[0])
    
    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.

    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    
    def calculate_score(cards):
        """Take a list of cards and return the score calculated from the cards."""
        if sum(cards) == 21:
            return 0
        elif sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            return sum(cards)
        else:
            return sum(cards)
    
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    def print_score(user_cards, computer_cards):
        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    
    def end_game(user_cards, computer_cards):
        if calculate_score(user_cards) == 21 and calculate_score(computer_cards) == 21:
            print_score(user_cards, computer_cards)
            print("Draw...")
            return 'y'
        elif calculate_score(user_cards) == 0 or calculate_score(computer_cards) > 21:
            print_score(user_cards, computer_cards)
            print("You Win!!!")
            return 'y'
        elif calculate_score(user_cards) > 21:
            print_score(user_cards, computer_cards)
            print("You went over. You lose")
            return 'y'
        elif calculate_score(computer_cards) == 0:
            print_score(user_cards, computer_cards)
            print("You lose")
            return 'y'
        else:
            return 'n'

    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    
    end = end_game(user_cards, computer_cards)
    another_card = 'y'
    while end == 'n' and another_card == 'y':
        if calculate_score(user_cards) < 21 and calculate_score(user_cards) != 0:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == "y":
                user_cards.append(deal_card())
                end = end_game(user_cards, computer_cards)
                if end == 'n':
                    print(f"    Your cards: {user_cards}, current score: {sum(user_cards)}")
                    print("    Computer's first card: ", computer_cards[0])
    
    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

    while end == 'n':
        if calculate_score(computer_cards) < 17 and calculate_score(computer_cards) != 0:
                computer_cards.append(deal_card())
                end = end_game(user_cards, computer_cards)
        else:
            break
    
    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

    def compare(user_score, computer_score):
        print_score(user_cards, computer_cards)
        if user_score == computer_score:
            print("Draw...")
        elif computer_score > user_score:
            print("You lose")
        else:
            print("You win!!!")

    if end == 'n':
        compare(calculate_score(user_cards), calculate_score(computer_cards))
    
    #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

print("Thank you...!")
