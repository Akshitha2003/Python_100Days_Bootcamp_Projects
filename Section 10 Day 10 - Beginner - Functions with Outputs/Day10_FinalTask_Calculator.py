# Calculator
from art import logo


# Add
def add(n1, n2):
    return n1+n2

# Subtract
def subtract(n1, n2):
    return n1-n2

# Multiply
def multiply(n1, n2):
    return n1*n2

# Divide
def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    operation = input("Pick an operation from the line above: ")
    num2 = float(input("What's the second number?: "))
    answer = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer} or to start a new calculation.: ")
    
    while choice == "y":
        prev_ans = answer
        operation = input("Pick and operation: ")
        next_num = float(input("What's the next number?: "))
        answer = operations[operation](prev_ans, next_num)
        print(f"{prev_ans} {operation} {next_num} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation.: ")

    if choice == "n":
        calculator()

calculator()