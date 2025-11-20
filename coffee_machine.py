# menu and resources dictionaries supplied as starting code
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
    "Money": 0
}

stop = False


def verify(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def get_coins(cost, drink):
    print("Please insert coins : ")
    quarters = float(input("How many Quarters  : "))
    dimes = float(input("How many Dimes  : "))
    nickles = float(input("How many Nickles  : "))
    pennies = float(input("How many Pennies  : "))
   

    total = (quarters * 0.25 + dimes * 0.10 +
             nickles * 0.05 + pennies * 0.01)

    if total < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    

    change = total - cost
    if change > 0:
        print(f"Here is ${round(change, 2)} in change.")

    print(f"Here is your {drink}. Enjoy!")
    resources["Money"] += cost

    return True


def deduct_resources(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]


def report(My_Liste):
    for key in My_Liste:
        print(f"{key} : {My_Liste[key]}")


# ---------------- MAIN LOOP ----------------
while not stop:
    your_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if your_choice == "off":
        stop = True

    elif your_choice == "report":
        report(resources)

    elif your_choice in ["espresso", "latte", "cappuccino"]:
        if verify(your_choice):  # Check resources first
            if get_coins(MENU[your_choice]["cost"], your_choice):  # Payment
                deduct_resources(your_choice)
            report(resources)  # Deduct ingredients
        else:
            stop = True

    else:
        print("Invalid choice, please select espresso/latte/cappuccino.")
