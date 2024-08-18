from ItemToPurchase import ItemToPurchase
from functools import reduce
import os

class ShoppingCart(object):
    customer_name: str
    current_date: str
    __items: dict[str, ItemToPurchase]
    
    def __init__(self, name: str = "none", today: str = "January 1, 2020") -> None:
        self.customer_name = name
        self.current_date = today
        self.__items = {}

        
    def add_item(self, item: ItemToPurchase) -> None:
            self.__items[item.item_name] = item
    
    def get_item_by_name(self, name: str) -> ItemToPurchase | None:
        return self.__items[name] if name in self.__items else None
            
    def remove_item(self, item_name: str) -> None:
        if item_name in self.__items:
            self.__items.pop(item_name)
        else: 
            print("Item not found in cart. Nothing removed.")
        
    def modify_item(self, item: ItemToPurchase) -> None:
        if item.item_name in self.__items:
            if item:
                self.__items[item.item_name] = item
        else:
            print("Item not found in cart. Nothing modified.")
    
    def get_num_items_in_cart(self) -> int: return reduce(lambda l, r: l + r, [i.item_quantity for i in self.__items.values()], 0)
    
    def get_cost_of_cart(self) -> float: return reduce(lambda l, r: l + r, [i.total() for i in self.__items.values()], 0)
            
    def print_total(self) -> str:
        check = f"{self.customer_name}'s Shopping cart - {self.current_date}" + os.linesep
        total = 0.0
        items = self.__items.values()
        for item in items:
            check += item.print_item_cost() + os.linesep
            total += item.total()
        return check + f"Total:{total}" 
    
    def print_descriptions(self) -> str:
        msg = f"{self.customer_name}'s Shopping cart - {self.current_date}" + os.linesep
        items = self.__items.values()
        for item in items:
            msg += item.get_description()
        return msg