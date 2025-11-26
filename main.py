from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#your_choice = input("choisir votre caffee (espresso/latte/capucino) : ")
money_machine = MoneyMachine()

menu = Menu()
coffee_maker = CoffeeMaker()


is_on = True

while is_on:
    option = menu.get_items()
    choice = input(f"input your choice {option} : ")
    if choice == "off":
        is_on=False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink=drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


