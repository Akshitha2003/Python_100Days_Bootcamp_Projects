from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)
print("Welcome to the secret auction program.")

data = {}

name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
data[name] = bid

choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
clear()

while choice == "yes":
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  data[name] = bid
  
  choice = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()

max_bid = 0
max_bidder = ""
for key in data:
  if data[key]>max_bid:
    max_bid = data[key]
    max_bidder = key

print(f"The winner is {max_bidder} with a bid of ${max_bid}.")