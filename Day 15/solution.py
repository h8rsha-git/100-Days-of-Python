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
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${machine_total}")


def calculate_total():
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


def check_resources(drink):
    for resource in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def update_resources(drink):
    for resource in MENU[drink]['ingredients']:
        resources[resource] -= MENU[drink]['ingredients'][resource]


def process_coins(drink):
    user_total = calculate_total()
    coffee_cost = MENU[drink]['cost']
    if coffee_cost <= user_total:
        update_resources(user_input)
        change = user_total - coffee_cost
        if change > 0:
            print(f"Here is ${round(change, 2)} dollars in change.")
        print(f"Here is your {user_input}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


state = 'ON'
machine_total = 0
# OFF CASE

while state == 'ON':
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    if user_input.lower() == 'report':
        print_report()
    elif user_input.lower() == 'off':
        state = 'OFF'
    else:
        # process coins
        if check_resources(user_input):
            process_coins(user_input)
            machine_total += MENU[user_input]['cost']



