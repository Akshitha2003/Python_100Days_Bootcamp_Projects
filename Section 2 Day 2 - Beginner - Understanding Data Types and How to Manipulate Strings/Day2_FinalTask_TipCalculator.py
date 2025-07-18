#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
tot_bill = float(input("What was the total bill? $"))
per = int(input("What percent tip would you like to give? 10, 12, or 15? "))
n = int(input("How many people to split the bill? "))
# amt = round((tot_bill/n)*(1+(per/100)), 2) # Gives 22.9 instead of 22.90
amt = "{:.2f}".format((tot_bill/n)*(1+(per/100)))
print(f"Each person should pay: ${amt}")