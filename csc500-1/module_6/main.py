from ShoppingCart import ShoppingCart
from store_front import StoreFront
from datetime import date
from os import system

if __name__ == '__main__':  
    system("cls")
    print("Welcome to our store!")
    name = input("Please enter you name:")
    today = str(date.today())
    cart = ShoppingCart(name, today)
    store = StoreFront(input)
    store.print_menu(cart)