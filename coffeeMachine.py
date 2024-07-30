from data import MENU, resources


profit = 0
def is_resource_sufficient(order_ingredients):
    """returns true if the ingredients are sufficient for order made"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, {item} is not sufficient")
            return False
    return True

def process_coins():
    """returns total calculated from coins inserted"""
    print("please insert coins")
    total = int(input("How many quarters do you have? "))*0.25
    total +=int(input("How many dimes do you have? ")) * 0.1
    total +=int(input("How many nickles do you have? ")) * 0.05
    total +=int(input("How many pennies do you have? ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """returns true if the money received is sufficient for transaction"""
    if money_received >= drink_cost:
        change = money_received - drink_cost
        print(f"You have ${change} in change")
        global profit
        profit = profit + drink_cost
        return True
    else:
        print(f"Sorry, {money_received} is not enough for this transaction, Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """dispense the coffee is the resources are more than the ingredients"""
    for item in resources:
        resources[item] -= order_ingredients[item]
    print("Here's your coffee ☕")


is_on = True
while is_on:
    choice = input("What do you want, latte/cuppacino/espresso: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])




