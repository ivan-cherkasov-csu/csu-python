from typing import Any, Callable
from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
from input_util import str2number, get_splitter
            
class Command(object):
    __cmd: Callable[[ShoppingCart], str|None]
    __text: str
    def __init__(self, cmd: Callable[[ShoppingCart], str|None], text:str) -> None:
        self.__cmd = cmd
        self.__text = text
        
    def __call__(self, cart: ShoppingCart) -> str|None:
        print(self.__text.upper())
        return self.__cmd(cart)
    
    def __str__(self) -> str:
        return self.__text
    def __format__(self, __format_spec: str) -> str:
        return self.__text.__format__(__format_spec)

class StoreFront(object):
    __commands: dict[str, Command]
    __source: Callable[[str], str]
    __available: dict[str, ItemToPurchase]
    __name_str: str
    __quantity_str: str
    __quit: bool
    __width: int
    
    def __init__(self, source: Callable[[str],str]) -> None:
        self.__quit = False
        self.__name_str = "item_name"
        self.__quantity_str = "item quantity"
        self.__source = source
        self.__width = 70
        self.__commands = {
            "a": Command(self.add,"Add item to cart"),
            "r": Command(self.remove,"Remove item from cart"),
            "c": Command(self.modify,"Change item quantity"),
            "i": Command(self.descriptions,"Output items' descriptions"),
            "o": Command(self.total,"Output shopping cart"),
            "q": Command(self.quit,"Quit")
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
            print(f"|{item.get_description()}|")
    
    
    def print_menu_items(self) -> None:
        for k,v in self.__commands.items():
            print(f"| {k} - {v:<63}|")
    
    def print_menu(self, cart: ShoppingCart) -> None:
        cmd = ""
        print(f"Items for sale:".center(self.__width, "_"))
        self.print_available_items()
        print(get_splitter(self.__width))
        while not self.__quit:
            print("MENU".center(self.__width, "_"))
            self.print_menu_items()
            print(get_splitter(self.__width))
            cmd = self.__source("Choose an option: ").strip()
            if cmd == "q": return
            command = self.map_command(cmd)
            if command:
                command(cart)
            else: print(f"<{cmd}> is not a valid command")
            
    def map_command(self, name: str) -> Callable[[ShoppingCart], str|None]:
        if name in self.__commands:
            return self.__commands[name]
        else: return None
    
    def add(self, cart: ShoppingCart) -> None:
        item = ItemToPurchase()
        item = self.update_item(item)
        if item: cart.add_item(item)
        
    def remove(self, cart: ShoppingCart) -> None:
        name = self.__source("Please enter the name of item to remove:")
        if name is None: return 
        cart.remove_item(name)
        
    def modify(self, cart: ShoppingCart) -> None:
        name = self.__process_input(self.__name_str, self.__source, lambda s: self.check_availability(s)) 
        if name is None: return 
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
        
    def update_item(self, item: ItemToPurchase) -> ItemToPurchase|None:
        item.item_name = self.__process_input(self.__name_str, self.__source, lambda s: self.check_availability(s))
        item.item_quantity = self.__process_input(self.__quantity_str, self.__source, str2number)
        if item.item_name is None or item.item_quantity is None: return None
        item.item_description = self.__available[item.item_name].item_description
        item.item_price = self.__available[item.item_name].item_price
        return item
    
    def check_availability(self, name: str) -> str | None:
        if name in self.__available:
            return name
        else:
            print(f"Item '{name}' not available, available items:")
            print(get_splitter(self.__width))
            for n in self.__available.values():
                print(n.get_description())
            print(get_splitter(self.__width))
            return None
        
    def __process_input(self, prompt: str, source: Callable[[str],str], convert: Callable[[str],int|None] | Callable[[str],float|None]) -> int|float|None:
        while True:
            input = source(f"Enter the {prompt}: ")
            if input and input.strip() == "q":
                self.__quit = True
                return None
            value = convert(input)
            if value is not None: return value
            else: print(f"Incorrect input {input} for {prompt}, please try again...")
