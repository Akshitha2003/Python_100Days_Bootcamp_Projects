rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
  print("Invalid input.")
else:
  print(game_images[choice])
  computer = random.randint(0,2)
  print(f"Computer chose:\n{game_images[computer]}")
  
  if choice == 0:
    if computer == 1:
      print("You lose.")
    elif computer == 0:
      print("Draw!")
    else:
      print("You win!")
  elif choice == 1:
    if computer == 2:
      print("You lose.")
    elif computer == 1:
      print("Draw!")
    else:
      print("You win!")
  else:
    if computer == 0:
      print("You lose.")
    elif computer == 2:
      print("Draw!")
    else:
      print("You win!")