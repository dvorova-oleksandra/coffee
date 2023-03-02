import data


def print_report():
    """Input state of resources"""
    for key in data.resources:
        print(f"{key.title()} : {data.resources[key]}")
    print(f"Profit: {data.profit}")


def checking(type_coffee):
    """Check that is enough resources in machine"""
    coffee = data.MENU[type_coffee]["ingredients"]
    flag = False
    for key in coffee:
        if coffee[key]>data.resources[key]:
            flag = True
            break
    return flag


def change_resources(type_coffee):
    """Use resources for coffee from machine"""
    coffee = data.MENU[type_coffee]["ingredients"]
    data.profit += data.MENU[type_coffee]["cost"]
    for key in coffee:
        data.resources[key] -= coffee[key]


def coffee_done(type_coffee):
    """Take your coffee"""
    print(f"Here is your {type_coffee} ☕ Enjoy!")


def insert_coin():
    """Inserting money in machine"""
    money = {"quaters": 0, "dimes":0, "nickles":0, "pennies":0}
    for key in money:
        money[key] = input(f"How many {key}? : ")
    return money

def sum_money():
    """Calculate coins to sum"""
    coins = insert_coin()
    total = int(coins["quaters"])*25 + int(coins["dimes"])*10 + int(coins["nickles"])*5 + int(coins["pennies"])
    dollars = total/100
    return round(dollars, 2)


def enough_money(type_coffee, dol):
    """Checking that person insert enough money"""
    flag = False
    cost = data.MENU[type_coffee]["cost"]
    if dol < cost:
        flag = True
    return flag


def info_change(type_coffee, dol):
    """Calculate change of money"""
    cost = data.MENU[type_coffee]["cost"]
    change = dol - cost
    if dol > cost:
        print(f"Here is {round(change, 2)}$ in change.")


def work_with_coffee(type_coffee):
    """Checking all aspects for making coffee"""
    if checking(type_coffee) == False:
        dol = sum_money()
        if enough_money(type_coffee, dol) == False:
            info_change(type_coffee, dol)
            change_resources(type_coffee)
            coffee_done(type_coffee)
        else:
            print("It is not enough money")


def work_with_input(data_input):
    """Make action"""
    flag = True
    if data_input == "report":
        print_report()
    elif data_input == "espresso" or data_input == "latte" or data_input == "cappuccino":
        work_with_coffee(data_input)
    else:
        flag = False
    return flag


def main():
    """Create cycle for working machine"""
    while True:
        inputing = input("What would you like? (espresso/latte/cappuccino): ")
        if work_with_input(inputing) == False:
            break



if __name__ == '__main__':
    main()
