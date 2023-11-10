from requirements import print_resource_report
from requirements import espresso_satisfaction, latte_satisfaction, cappuccino_satisfaction
from requirements import get_money, calculate_amount, get_balance
from requirements import update_resources
from items import MENU, resources

users_need = input("What would you like? (espresso/latte/cappuccino): ")
money = 0.0

while users_need != "off":
    if users_need == "report":
        print_resource_report(resources=resources, money=money)
    elif users_need == "espresso":
        if espresso_satisfaction(resources=resources):
            paid_amount = get_money()
            total_amount_paid = calculate_amount(amount=paid_amount)
            if total_amount_paid >= MENU["espresso"]["cost"]:
                balance_amount = get_balance(item="espresso", total_amount_paid=total_amount_paid)
                print("Here is your espresso ☕ Enjoy!")
                resources = update_resources(item="espresso", resources=resources)
                money += (total_amount_paid - balance_amount)
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif users_need == "latte":
        if latte_satisfaction(resources=resources):
            paid_amount = get_money()
            total_amount_paid = calculate_amount(amount=paid_amount)
            if total_amount_paid >= MENU["latte"]["cost"]:
                balance_amount = get_balance(item="latte", total_amount_paid=total_amount_paid)
                print("Here is your latte ☕ Enjoy!")
                resources = update_resources(item="latte", resources=resources)
                money += (total_amount_paid-balance_amount)
            else:
                print("Sorry that's not enough money. Money refunded.")

    elif users_need == "cappuccino":
        if cappuccino_satisfaction(resources=resources):
            paid_amount = get_money()
            total_amount_paid = calculate_amount(amount=paid_amount)
            if total_amount_paid >= MENU["cappuccino"]["cost"]:
                balance_amount = get_balance(item="cappuccino", total_amount_paid=total_amount_paid)
                print("Here is your cappuccino ☕ Enjoy!")
                resources = update_resources(item="cappuccino", resources=resources)
                money += (total_amount_paid-balance_amount)
            else:
                print("Sorry that's not enough money. Money refunded.")

    users_need = input("What would you like? (espresso/latte/cappuccino): ")
