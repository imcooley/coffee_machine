MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def format_report():
    """Request a report of remaining resources in the machine."""
    return f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g' \
           f'\nMoney: ${resources["money"]}'


def check_resources(coffee_choice):
    """Check to see if there is enough ingredients remaining to process request."""
    if MENU[coffee_choice]["ingredients"]["water"] >= resources["water"]:
        return "water"
    elif MENU[coffee_choice]["ingredients"]["coffee"] >= resources["coffee"]:
        return "coffee"
    elif coffee_choice == "espresso":
        return 0
    elif MENU[coffee_choice]["ingredients"]["milk"] >= resources["milk"]:
        return "milk."
    else:
        return 0


def process_payment(inst_quarters, inst_dimes, inst_nickles, inst_pennies, coffee_choice):
    """Process the money transaction. Make change and refund if not enough was provided."""
    money_total = 0
    money_total += inst_quarters * .25
    money_total += inst_dimes * .10
    money_total += inst_nickles * .05
    money_total += inst_pennies * .01
    if money_total >= MENU[coffee_choice]["cost"]:
        customer_change = money_total - MENU[coffee_choice]["cost"]
        resources["money"] += MENU[coffee_choice]["cost"]
        return round(customer_change, 2)
    else:
        return 0
    # resources["money"] += money_total


def make_coffee(coffee_choice):
    """Make the coffee and remove the resources once consumed. """
    # for ingredient in MENU[coffee_choice]["ingredients"]:
    #     print(MENU[coffee_choice]["ingredients"])
    resources["water"] -= MENU[coffee_choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_choice]["ingredients"]["coffee"]
    if coffee_choice == "espresso":
        return f"Here is your {coffee_choice} ☕️. Enjoy!"
    resources["milk"] -= MENU[coffee_choice]["ingredients"]["milk"]
    return f"Here is your {coffee_choice} ☕️. Enjoy!"


should_continue = True

while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "report":
        print(format_report())
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    elif choice == "off":
        should_continue = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        enough_resources = check_resources(choice)
        if enough_resources == "water" or enough_resources == "coffee" or enough_resources == "milk":
            print(f"Sorry there is not enough {enough_resources}.")
        elif enough_resources == 0:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            change = process_payment(quarters, dimes, nickles, pennies, choice)
            if change == 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is ${change} in change.")
                make_coffee(choice)
    else:
        print("You make choose an invalid option.")
