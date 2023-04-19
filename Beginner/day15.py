# day 15
# coffee machine project
from database import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
isOn = True
profit = 0


def printReport():
    print(
        f"Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n Coffee: {resources['coffee']}ml\nMoney: ${profit}")


def isResourceSufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"caunt make it not enough {item}")
            return False
    return True


def processCoins():
    print("pls insert coins")
    total = 0
    total += int(input("How many quarters")) * .25
    total += int(input("how many Dimes")) * .1
    total += int(input("how many nickles")) * 0.05
    total += int(input("How many pennies")) * 0.01
    return total


def isTransactionSuccessful(money, drinkCost, profit):
    if money >= int(drinkCost):
        change = round(money - drinkCost, 2)
        print(f"here is ${change}in change")
        profit += drinkCost
        return True
    else:
        print('Not Enough money, Refunding...')
        return False


def makeCoffee(drinkName, order_ing):
    for item in order_ing:
        resources[item] -= order_ing[item]
        print(f"here is ur drink sir{drinkName}")


while isOn:
    coffee = input("What would you like(Espresso/latte/cappuccino)")
    if coffee == 'off':
        isOn = False
    elif coffee == 'report':
        printReport()
    else:
        drink = MENU[coffee]
        if isResourceSufficient(drink['ingredients']):
            payment = processCoins()
            isTransactionSuccessful(payment, drink['cost'], profit)
            makeCoffee(coffee, drink["ingredients"])
