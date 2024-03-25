from typing import Callable
from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
from input_util import str2number

class StoreFront(object):
    __commands: dict[str, Callable[[ShoppingCart], None| str]]
    __source: Callable[[str], str]
    __available: dict[str, ItemToPurchase]
    __name_str: str
    __quantity_str: str
    __quit: bool
    
    def __init__(self, source: Callable[[str],str]) -> None:
        self.__quit = False
        self.__name_str = "item_name"
        self.__quantity_str = "item quantity"
        self.__source = source
        self.__commands = {
            "a": self.add,
            "r": self.remove,
            "c": self.modify,
            "i": self.descriptions,
            "o": self.total
        }
        self.__available = {
           "Earbuds": ItemToPurchase("Earbuds", 29.73, 0, "Bluetooth IEMs"), 
           "Solar Panel": ItemToPurchase("Solar Panel", 379.00, 0, "220 Watt bi-facial"), 
           "Batteries": ItemToPurchase("Batteries", 6.99, 0, "AAA batteries, 24 pack"), 
           "Doorbell": ItemToPurchase("Doorbell", 59.99, 0, "1080p video, improved motion detection"), 
           "Speaker": ItemToPurchase("Speaker", 129.95, 0, "Portable Wireless Bluetooth Speaker"), 
        }
    
    def print_available_items(self) -> None:
        for item in self.__available.values():
            print(item.get_description())
    
    def print_menu(self, cart: ShoppingCart) -> None:
        cmd = ""
        print("Items for sale:")
        self.print_available_items()
        while not self.__quit:
            print("""
                  MENU
            a - Add item to cart
            r - Remove item from cart
            c - Change item quantity
            i - Output items' descriptions
            o - Output shopping cart
            q - Quit""")
            cmd = self.__source("Choose an option:").strip()
            if cmd == "q": return
            command = self.map_command(cmd)
            if command:
                try: command(cart)
                except: pass
            else: print(f"<{cmd}> is not a valid command")
            
    def map_command(self, name: str) -> Callable[[ShoppingCart], None| str]:
        if name in self.__commands:
            return self.__commands[name]
        else: return None
    
    def add(self, cart: ShoppingCart) -> None:
        item = ItemToPurchase()
        item = self.update_item(item)
        cart.add_item(item)
        
    def remove(self, cart: ShoppingCart) -> None:
        name = self.__source("Please enter the name of item to remove:")
        cart.remove_item(name)
        
    def modify(self, cart: ShoppingCart) -> None:
        name = self.__process_input(self.__name_str, self.__source, lambda s: self.check_availability(s)) 
        item = cart.get_item_by_name(name)
        if item:
            item.item_quantity = self.__process_input(self.__quantity_str, self.__source, str2number)
        else:
            print("Item not found in cart.")
            
    def print_total(self, cart: ShoppingCart) -> None:
        print(cart.print_total())
        
    def descriptions(self, cart: ShoppingCart) -> None:
        print(cart.print_descriptions())
    
    def total(self, cart: ShoppingCart) -> None:
        print(cart.print_total())
        
    def quit(self, cart: ShoppingCart) -> None: self.__quit = True
        
    def update_item(self, item: ItemToPurchase) -> ItemToPurchase:
        item.item_name = self.__process_input(self.__name_str, self.__source, lambda s: self.check_availability(s))
        item.item_description = self.__available[item.item_name].item_description
        item.item_price = self.__available[item.item_name].item_price
        item.item_quantity = self.__process_input(self.__quantity_str, self.__source, str2number)
        return item
    
    def check_availability(self, name: str) -> str | None:
        if name in self.__available:
            return name
        else:
            print("item not available, available items:")
            for n in self.__available.keys():
                print(n)
            return None
        
    def __process_input(self, prompt: str, source: Callable[[str],str], convert: Callable[[str],int|None] | Callable[[str],float|None]) -> int|float|None:
        while True:
            input = source(f"Enter the {prompt}: ")
            if input and input.strip() == "q":
                self.__quit = True
                raise Exception("quit")
            value = convert(input)
            if value is not None: return value
            else: print(f"Incorrect input {input} for {prompt}, please try again...")