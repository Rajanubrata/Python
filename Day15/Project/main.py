from Menue import resources
from Menue import MENU
from os import system
import art
empty = []

print(art.logo)
print(art.sign)


def update_resource(coffee):
    if Coffee == "espresso":
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]


def check_resource(coffee):
    for items in MENU[coffee]["ingredients"]:
        if resources[items] < MENU[coffee]["ingredients"][items]:
            empty.append(items)
            return False
    return True


def change(total_money, coffee):
    return total_money-MENU[coffee]["cost"]


def report():
    for items in resources:
        print(items + " : " + str(resources[items]))


Run = True
while Run:
    # TODO: 1.Take user choice of coffee
    Coffee = input("What would you like? \n☕espresso(124.23Rs.)\n☕latte(207.05Rs.)\n☕cappuccino(248.46Rs.)\n:")
    if Coffee == "resource":
        report()
        continue
    # TODO: 2.Take money and give change
    print("Please Insert Coins")
    five = int(input("5 Rs. Coin: "))
    Ten = int(input("10 Rs. Coin: "))
    fifty = int(input("50 Rs. Coin: "))

    Total_Money = five*5 + Ten*10 + fifty*50

    if Total_Money >= MENU[Coffee]["cost"]:
        if check_resource(Coffee):
            update_resource(Coffee)
            # TODO: 3.Give coffee to user
            print(f"Here is your {Coffee}☕. Enjoy!")
            Change = change(Total_Money, Coffee)
            print(f"Here is Your Change : {Change} Rs.")
        else:
            print(f"Sorry there is not enough {empty[0]}.")
            print("Your money is refunded")
    else:
        print("Sorry that's not enough money. Money refunded.")
    if input("Do you want to continue ? (Y/N)").lower() == "n":
        Run = False


