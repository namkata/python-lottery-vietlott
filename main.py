from vietlott_mega655 import random_ticket, buffet_ticket

if __name__ == "__main__":
    menu = {
        "1": "Buy a random ticket",
        "2": "Buy a buffet ticket",
        "3": "Jackpot Result",
        "4": "Exit"
    }
    while True:
        options = menu.keys()
        print("The menu:")
        print("1: Buy a random ticket")
        print("2: Buy a buffet ticket")
        print("3: Jackpot Result")
        print("4: Exit")
        selected = int(input("Please choose from the menu:"))
        if selected == 1:
            print("Your ticket:", random_ticket())
        elif selected == 2:
            print("Please enter 6 numbers you want to buy")
            number_first = int(input("Number first:"))
            number_two = int(input("Number two:"))
            number_three = int(input("Number three:"))
            number_four = int(input("Number four:"))
            number_five = int(input("Number five:"))
            number_six = int(input("Number six:"))
            ticket = buffet_ticket(number_first, number_two, number_three, number_four, number_five, number_six)
            if not ticket:
                print("Your ticket is not valid, please enter again:")
            else:
                print("Your ticket:", random_ticket())
        elif selected == 3:
            print("The jackpot:", random_ticket())
        elif selected == 4:
            break
        else:
            print("This request is not in the system")
            break
