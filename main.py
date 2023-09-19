from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe = CoffeeMaker()
money = MoneyMachine()

status = True

while status:
    options = menu.get_items()
    choice = input(f"what would you like? {options} ")
    if choice == "off":
        status = False

    elif choice == "report":
        coffe.report()
        money.report()

    else:
        drink = menu.find_drink(choice)
        if money.make_payment(drink.cost) and coffe.is_resource_sufficient(drink) is True:
            coffe.make_coffee(drink)
