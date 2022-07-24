state = 'ON'
profit = 0

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
}


def print_report():
    """Prints the current quantities of the resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def process_coins():
    print("Please insert coins.")
    total = 0
    quarters = int(input("How many quarters ?"))
    total += (0.25 * quarters)
    dimes = int(input("How many dimes ?"))
    total += (0.1 * dimes)
    nickels = int(input("How many nickels ?"))
    total += (0.05 * nickels)
    pennies = int(input("How many pennies ?"))
    total += (0.01 * pennies)
    return total


def is_resource_sufficient(drink):
    for resource in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def make_coffee(drink):
    for resource in MENU[drink]['ingredients']:
        resources[resource] -= MENU[drink]['ingredients'][resource]


def is_transaction_successful(drink):
    user_total = process_coins()
    coffee_cost = MENU[drink]['cost']
    if coffee_cost <= user_total:
        change = round(user_total - coffee_cost, 2)
        if change > 0:
            print(f"Here is ${change} dollars in change.")
        global profit
        profit += coffee_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



# OFF CASE

while state == 'ON':
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice.lower() == 'report':
        print_report()
    elif choice.lower() == 'off':
        state = 'OFF'
    else:
        # process coins
        if is_resource_sufficient(choice):
            payment = process_coins()
            if is_transaction_successful(choice):
                make_coffee(choice)




