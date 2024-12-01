MENU = {
    "espresso": {
        "ingredients": {
            "water": 20,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("What would you like? (espresso/latte/cappuccino): ")

makeMoreCoffe = True
while makeMoreCoffe == True:
    wantWhat = input("What do you want? ").lower()
    
    if wantWhat == "off":
        print("Good bye!")
        makeMoreCoffe = False
        
    elif wantWhat == 'report':
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
            
    elif wantWhat in MENU:
        drinks = wantWhat
        if resources["water"] < MENU[drinks]["ingredients"]["water"]:
            print("“Sorry there is not enough water.")
        elif resources["coffee"] < MENU[drinks]["ingredients"]["coffee"]:
            print("“Sorry there is not enough Coffee.")
        elif drinks != "espresso" and resources["milk"] < MENU[drinks]["ingredients"]["milk"]:
            print("“Sorry there is not enough Milk.")
        else:
            quarters = float(input("How many quaters "))
            dimes = float(input("How many dimes "))
            nickles = float(input("How many nickles "))
            pennies = float(input("How many  pennies "))

            # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
            totalPrice = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
            if totalPrice < MENU[drinks]["cost"]:
                print("Sorry that's not enough money. Money refunded. ")
            else:
                if totalPrice > MENU[drinks]["cost"]:
                   change = totalPrice - MENU[drinks]["cost"]
                   resources["money"] = f"${totalPrice}"

                   print(f"You spent {round(totalPrice, 2)}. Here is ${round(change, 2)} dollars in change. \n")
                   resources["water"] -=  MENU[drinks]["ingredients"]["water"]
                   resources["coffee"] -= MENU[drinks]["ingredients"]["coffee"]
                   resources["milk"] -= MENU[drinks]["ingredients"]["milk"]
                   print(f"Here is your {drinks}. Enjoy!")
                else:
                   resources["money"] = totalPrice
                   resources["water"] -=  MENU[drinks]["ingredients"]["water"]
                   resources["coffee"] -= MENU[drinks]["ingredients"]["coffee"]
    else:
        print("Enter a valid input. Report to see resources, (espresso/latte/cappuccino) to make any of them or 'off' ")
        makeMoreCoffe = False
        


            
