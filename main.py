MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18
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
    "money": 0
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${'{:.2f}'.format(resources['money'])}")


def print_menu():
    print("===================| MENU |=======================")
    print("Espresso....................................$1 .50")
    print("Latte.......................................$2 .50")
    print("Cappuccino..................................$3 .00")
    print("==================================================")


def prompt():
    user_input = input("Would you like a report of the system's resources? (Y or N)\n").lower()
    if user_input == "off":
        return user_input
    elif user_input == 'y':
        print_report()
    user_input = input("Which kind of coffee would you like to order?\n").lower()
    return user_input


def check_resources(beverage):
    water = True
    milk = True
    coffee = True

    if resources["water"] < MENU[beverage]["ingredients"]["water"]:
        water = False
    if resources["milk"] < MENU[beverage]["ingredients"]["milk"]:
        milk = False
    if resources["coffee"] < MENU[beverage]["ingredients"]["coffee"]:
        coffee = False

    if not water and not milk and not coffee:
        print("Sorry there is not enough water, milk, and coffee.")
        return False
    elif not water and not milk:
        print("Sorry there is not enough water and milk.")
        return False
    elif not water and not coffee:
        print("Sorry there is not enough water and coffee.")
        return False
    elif not milk and not coffee:
        print("Sorry there is not enough milk and coffee.")
        return False

    return True


def process_transaction(beverage):
    cost_of_beverage = 0
    if beverage == "espresso":
        print(f"That will be ${'{:.2f}'.format(MENU['espresso']['cost'])}")
        cost_of_beverage = MENU['espresso']['cost']
    elif beverage == "latte":
        print(f"That will be ${'{:.2f}'.format(MENU['latte']['cost'])}")
        cost_of_beverage = MENU['latte']['cost']
    elif beverage == "cappuccino":
        print(f"That will be ${'{:.2f}'.format(MENU['cappuccino']['cost'])}")
        cost_of_beverage = MENU['cappuccino']['cost']

    quarters = int(input("Please enter the number quarters you will enter: "))
    dimes = int(input("Please enter the number of dimes you will enter: "))
    nickels = int(input("Please enter the number nickels you will enter: "))
    pennies = int(input("Please enter the number of pennies you will enter: "))

    amount_entered = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

    while amount_entered < cost_of_beverage:
        print("That is not enough money.")
        decision = input("Would you like to cancel your order? (Y or N)\n").lower()
        if decision == 'y':
            return True
        print("Please re-enter your coins.")

        quarters = int(input("Quarters: "))
        dimes = int(input("Dimes: "))
        nickels = int(input("Nickels: "))
        pennies = int(input("Pennies: "))

        amount_entered = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

    if amount_entered > MENU[beverage]["cost"]:
        print("You entered more money than necessary. Processing Change...")
        change = amount_entered - MENU[beverage]["cost"]
        print(f"Your change is ${'{:.2f}'.format(change)}")

    resources["money"] += MENU[beverage]["cost"]


def update_resources(beverage):
    resources["water"] -= MENU[beverage]["ingredients"]["water"]
    resources["milk"] -= MENU[beverage]["ingredients"]["milk"]
    resources["coffee"] -= MENU[beverage]["ingredients"]["coffee"]


def coffee_machine():
    machine_on = True

    while machine_on:
        resource_sufficient = True
        print_menu()

        user_input = prompt()

        if user_input == "off":
            machine_on = False
            break
        elif user_input in MENU:
            resource_sufficient = check_resources(user_input)
            if not resource_sufficient:
                print(
                    f"This machine does not have the resources needed to make a {user_input}. We sincerely apologize.")
                continue
        else:
            print("Invalid Output. Please order a beverage from the menu.")
            continue

        transaction = process_transaction(user_input)
        if transaction:
            continue
        update_resources(user_input)
        print("Thank you for your patronage! Enjoy your coffee!")


coffee_machine()
