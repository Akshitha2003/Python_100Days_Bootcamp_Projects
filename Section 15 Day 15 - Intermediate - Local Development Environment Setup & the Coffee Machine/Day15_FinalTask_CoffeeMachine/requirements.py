from items import MENU


def print_resource_report(resources, money):
    """Gets the money and prints the resources available in a printable format."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${round(money, 2)}")


def espresso_satisfaction(resources):
    """Return True if the available resources are sufficient for making espresso."""
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
        if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            print("Sorry there is not enough coffee.")
            return False
    else:
        print("Sorry there is not enough water.")
        return False


def latte_satisfaction(resources):
    """Return True if the available resources are sufficient for making latte."""
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough milk.")
            return False
    else:
        print("Sorry there is not enough water.")
        return False


def cappuccino_satisfaction(resources):
    """Return True if the available resources are sufficient for making cappuccino."""
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
        if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee.")
                return False
        else:
            print("Sorry there is not enough milk.")
            return False
    else:
        print("Sorry there is not enough water.")
        return False


def get_money():
    """Accepts the money from the user and returns it as a dictionary."""
    print("Please insert coins.")
    paid_amount = {"quarters": int(input("How many quarters?: ")), "dimes": int(input("How many dimes?: ")),
                   "nickles": int(input("How many nickles?: ")), "pennies": int(input("How many pennies?: "))}
    return paid_amount


def calculate_amount(amount):
    """Calculates and returns the total amount paid by the user."""
    return round(amount["quarters"]*0.25 + amount["dimes"]*0.10 + amount["nickles"]*0.05 + amount["pennies"]*0.01, 2)


def get_balance(item, total_amount_paid):
    """Calculates and returns the excess of amount paid by the user if any."""
    if MENU[item]["cost"] != total_amount_paid:
        print(f"Here is ${round(total_amount_paid - MENU[item]["cost"], 2)} in change.")
        return round(total_amount_paid - MENU[item]["cost"], 2)


def update_resources(item, resources):
    """Update and returns the updated resource quantities."""
    if item == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[item]["ingredients"]["water"]
        resources["milk"] -= MENU[item]["ingredients"]["milk"]
        resources["coffee"] -= MENU[item]["ingredients"]["coffee"]
    return resources
