from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True

menu_class = Menu()
coffee_class = CoffeeMaker()
money_class = MoneyMachine()

while machine_on:
    chose = input(f"What would you like? {Menu().get_items()} : ").lower()
    if chose == 'off':
        machine_on = False
    elif chose == 'report':
        coffee_class.report()
        money_class.report()
    # elif menu_class.find_drink(chose):
    else:
        # Check this point of the program
        drink = menu_class.find_drink(chose)
        if coffee_class.is_resource_sufficient(drink) and money_class.make_payment(drink.cost):
            coffee_class.make_coffee(drink)

