from ShoppingCart import ShoppingCart
from StoreFront import StoreFront
from datetime import date, datetime
from os import system

if __name__ == '__main__':  
    system("cls")
    print("Welcome to our store!")
    name = input("Please enter you name:")
    dateFormat = "%m/%d/%Y"
    today = date.today().strftime(dateFormat)
    print(f"Hello, {name}! Today is {today}.")
    while True:
        d = input("Enter date using following format 'mm/dd/yyyy' or enter empty line to leave it as is:")
        if not d: break
        try:
            today = datetime.strptime(d, dateFormat).date().strftime(dateFormat)
            print(f"The date set to {today}.")
            break
        except: print(f"Cannot parse value {d}")
    cart = ShoppingCart(name, today)
    store = StoreFront(input)
    store.print_menu(cart)