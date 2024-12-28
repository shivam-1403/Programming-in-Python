from menu_resource_data import MENU, resources

profit = 0

def is_resource_sufficint(order_ingredients) :
    """Returns True when order can be made, and False if ingredients are insufficient."""
    for item in order_ingredients :
        if order_ingredients[item] >= resources[item] :
            print(f"Sorry there is not enough {item}")
            return False
    return True
        

def process_coins() :
    """Return the total calculated from coins inserted."""
    print("Please insert coins.")
    total = float(input("How many Quarters ? : ")) * 0.25
    total += float(input("How many Dimes ? : ")) * 0.1
    total += float(input("How many Nickels ? : ")) * 0.05
    total += float(input("How many Pennies ? : ")) * 0.01

    return total

def is_transaction_successful(money_recieved, drink_cost) :
    """Returns True when the money is accepted and False if money is insufficient."""
    if money_recieved >= drink_cost :
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else :
        print("Sorry that's not enough Money. Money Refunded.")
        return False
    
def make_coffee(drink_name, order_ingredients) :
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


end = False
while not end :
    choice = input("Type 'report' to see report and 'end' to end the Machine.\nWhat would you like ? (espresso/latte/cappuccino) : ")
    if choice == "end" :
        end = True
    elif choice == "report" :
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}gm")
        print(f"Money : ${profit}")
    else :
        drink = MENU[choice]
        if is_resource_sufficint(drink["ingredients"]) :
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]) :
                make_coffee(choice, drink["ingredients"])