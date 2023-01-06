from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
logo = """
             ;,'
     _o_    ;:;'
 ,-.'---`.__ ;
((j`=====',-'
 `-\     /
    `-=-'     """

print(logo)

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
isOn = True


while isOn:
    option = menu.get_items()
    choice = input(f"What would you like to have? ({option})")

    if choice == "off":
        isOn = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
