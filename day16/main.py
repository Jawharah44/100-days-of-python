from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_continue = True

while machine_continue:
    options = menu.get_items()
    user_request = input(f"What would you like? ({options}): ")
    if user_request == "off":
        game_continue = False
    elif user_request =="report":
        coffe_maker.report()
        money_machine.report()
        
    else:
        drink = menu.find_drink(user_request)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)