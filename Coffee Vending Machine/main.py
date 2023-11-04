


milk = 100
water = 200
coffee = 50
money = 0

# Updated prices
price_espresso = 60
price_latte = 80
price_cappuccino = 100

def take_money(cost):
    global money

    print(f'Please insert notes (10, 20, 50, or 100 Rupees) for {choice} ({cost} INR):')
    notes_10 = int(input('How many 10 Rupee notes: '))
    notes_20 = int(input('How many 20 Rupee notes: '))
    notes_50 = int(input('How many 50 Rupee notes: '))
    notes_100 = int(input('How many 100 Rupee notes: '))
    total_rupees = notes_10 * 10 + notes_20 * 20 + notes_50 * 50 + notes_100 * 100

    if total_rupees == cost:
         money += cost
         calculate_resource(cost)
         print(f'**** Take your {choice}... ****')
    elif total_rupees > cost:
         money += cost
         calculate_resource(cost)
         change = total_rupees - cost
         print(f'**** Here is your change of {change} INR, and enjoy your {choice} ****')
    else:
         needed_rupees = cost - total_rupees
         print(f'**** Not enough amount. You need to add {needed_rupees} INR... ****')

def calculate_resource(cost):
    global water
    global coffee
    global milk
    if cost == price_espresso:
        water -= 50
        coffee -= 18
    elif cost == price_latte:
        water -= 200
        coffee -= 24
        milk -= 150
    elif cost == price_cappuccino:
        water -= 250
        milk -= 150
        coffee -= 24

def check_reso(choice):
    if choice == 'espresso':
        if water >= 50 and coffee >= 18:
            cost = price_espresso
            take_money(cost)
        else:
            print('Not enough resources...')
    elif choice == 'latte':
        if water >= 200 and coffee >= 24 and milk > 150:
            cost = price_latte
            take_money(cost)
        else:
            print('Not enough resources...')
    elif choice == 'cappuccino':
        if water >= 250 and coffee >= 24 and milk >= 150:
           cost = price_cappuccino
           take_money(cost)
        else:
            print('Not enough resources...')

def coffee_machine(choice):
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        check_reso(choice)
    else:
        print(f'\n\nAvailable options:')
        print(f'1. Espresso - Price: {price_espresso} INR')
        print(f'2. Latte - Price: {price_latte} INR')
        print(f'3. Cappuccino - Price: {price_cappuccino} INR')
        print(f'Milk = {milk} ml')
        print(f'Water = {water} ml')
        print(f'Coffee = {coffee} gms')
        print(f'Money = {money} INR')

while True:
    choice = input(f' \n 1. Espresso - Price: {price_espresso} INR \n 2. Latte - Price: {price_latte} INR \n 3. Cappuccino - Price: {price_cappuccino} INR \n check resources? \n What would you like: ').lower()
    if(choice == 'break'):
        break
    coffee_machine(choice)

