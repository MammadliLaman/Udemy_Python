from main import menu, resources

quarters = 0.25
dimes = 0.4
nickles = 0.05
pennies = 0.01


def check_resources() -> (bool, str):
    required_water, required_milk, required_coffee = get_resources()
    water, milk, coffee = resources["water"], resources["milk"], resources["coffee"]

    if water >= required_water and milk >= required_milk and coffee >= required_coffee:
        return True, None
    elif water < required_water and milk >= required_milk and coffee >= required_coffee:
        return False, "Sorry there is not enough water."
    elif water >= required_water and milk < required_milk and coffee >= required_coffee:
        return False, "Sorry there is not enough milk."
    elif water >= required_water and milk >= required_milk and coffee < required_coffee:
        return False, "Sorry there is not enough milk."
    else:
        return False, "Sorry there is not enough resources."


def check_price(choice, coin_quarters, coin_dimes, coin_nickles,coin_pennies) -> (bool, str):
    total = round(
        (coin_quarters * quarters) + (coin_dimes * dimes) + (coin_nickles * nickles) + (coin_pennies * pennies))
    cost = menu[choice]["cost"]

    if total < cost:
        return False, "Sorry that's not enough money. Money refunded."

    return True, prepare_coffee(total, cost)


def prepare_coffee(total, cost):
    change = total - cost
    print(f"Here is {change} in change. \n Here is your {choice} ☕️. Enjoy!")
    up_water = resources["water"] - menu[choice]["ingredients"]["water"]
    up_milk = resources["milk"] - menu[choice]["ingredients"]["milk"]
    up_coffee = resources["coffee"] - menu[choice]["ingredients"]["coffee"]

    update_resources(up_water, up_milk, up_coffee)

    return f"Report after purchasing {choice}: \n" \
           f"Water: {up_water}, Milk: {up_milk}, Coffee: {up_coffee}"


def update_resources(water, milk, coffee):
    resources["water"] = water
    resources["milk"] = milk
    resources["coffee"] = coffee


def get_resources():
    return menu[choice]["ingredients"]["water"], menu[choice]["ingredients"]["milk"], menu[choice]["ingredients"][
        "coffee"]


start = input("If you want some coffee the type 'yes' or 'no'")

while start.lower() == 'y' or start.lower() == 'yes':
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    result, message = check_resources()
    if not result:
        print(message)
    else:
        print("Please insert coins.")
        coin_quarters = int(input("How many quarters?: "))
        coin_dimes = int(input("How many dimes?: "))
        coin_nickles = int(input("How many nickles?: "))
        coin_pennies = int(input("How many pennies?: "))

        result, message = check_price(choice, coin_quarters, coin_dimes, coin_nickles, coin_pennies)

        print(message)

        start = input("Do you want more?\nyes or no!")
