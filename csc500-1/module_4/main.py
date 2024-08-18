from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
import os

if __name__ == '__main__':  
    os.system("cls")
    print("Please fill you shopping cart")
    print("input item's name, price, and quantity on separate lines")
    print("you can put multiple items")
    print("NOTE adding item with same name will replace item in cart")
    print("input 'exit' or empty line to finish")
    cart = ShoppingCart(input)
    cart.fill_cart()
    check = cart.get_check()
    print("____________________________________________")
    print(check)
    print("____________________________________________")