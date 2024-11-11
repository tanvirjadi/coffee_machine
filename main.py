from coffe_menu import *
def subtract_ingredients(coffee, ingredient):
    resources[ingredient] -= MENU[coffee]["ingredients"][ingredient]
def transaction(coffee):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    if total >= MENU[coffee]["cost"]:
        change = round(total - MENU[coffee]["cost"], 2)
        print(f"Here is ${change} in change.")
    else:
        return False
def store_money(coffee):
    if "money" in resources:
        resources["money"] += MENU[coffee]["cost"]
    else:
        resources["money"] = MENU[coffee]["cost"]
is_machine_off = False
while not is_machine_off:
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order in MENU:
            if resources["water"] >= MENU[order]["ingredients"]["water"]:
                if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
                    if order != "espresso":
                        if resources["milk"] >= MENU[order]["ingredients"]["milk"]:
                            if not transaction(order) == False:
                                ingredients = ["water", "milk", "coffee"]
                                for ingredient in ingredients:
                                    subtract_ingredients(order, ingredient)
                                store_money(order)
                                print(f"Here is your {order} ☕. Enjoy!")
                            else:
                                print("Sorry that's not enough money. Money is refunded.")
                        else:
                            print(f"We don't have enough milk to make {order}. Money is refunded.")
                    else:
                        if not transaction(order) == False:
                            ingredients = ["water", "coffee"]
                            for ingredient in ingredients:
                                subtract_ingredients(order, ingredient)
                            store_money(order)
                            print("Here is your espresso ☕. Enjoy!")
                        else:
                            print("Sorry that's not enough money. Money is refunded.")
                else:
                    print(f"We don't have enough coffee to make {order}. Money is refunded.")
            else:
                print(f"We don't have enough water to make {order}. Money is refunded.")
        elif order == "report":
            secret_key = input("What is the secret key 🔐?: ")
            if secret_key == "TOPSECRET":
                for resource in resources:
                    if resource != "money":
                        print(f'{resource.title()}: {resources[resource]}ml')
                    else:
                        print(f'{resource.title()}: ${resources[resource]}')
            else:
                print("Invalid Key. Try again.")
        elif order == "off":
            is_machine_off = True
            print("Goodbye.")
        else:
            print(f"We don't have {order} type of coffee.")
    else:
        print("Now we don't have enough ingredients to make more coffees. Turn on the coffee machine again to restore ingredients.")
        is_machine_off = True
