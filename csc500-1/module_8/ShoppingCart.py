from ItemToPurchase import ItemToPurchase
from functools import reduce
from input_util import get_splitter, get_line


class ShoppingCart(object):
    customer_name: str
    current_date: str
    __items: dict[str, ItemToPurchase]
    __width: int
    
    def __init__(self, name: str = "none", today: str = "January 1, 2020") -> None:
        self.customer_name = name
        self.current_date = today
        self.__width = 70
        self.__items = {}
        
    def set_output_width(self, width: int) -> 'ShoppingCart':
        self.__width = width
        return self
        
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
        msg = get_line(get_splitter(self.__width))
        msg += get_line(f"{self.customer_name}'s Shopping cart - {self.current_date}".center(self.__width, "_"))
        msg += get_line(get_splitter(self.__width))
        total = 0.0
        items = self.__items.values()
        if items:
            for item in items:
                msg += get_line(item.print_item_cost())
                total += item.total()
            return msg + f"Total:{total}".center(self.__width, "_")
        else:
            return self.__get_empty_msg()
    
    def print_descriptions(self) -> str:
        msg = get_line(get_splitter(self.__width))
        msg += get_line(f"{self.customer_name}'s Shopping cart - {self.current_date}".center(self.__width, "_"))
        msg += get_line(get_splitter(self.__width))
        items = self.__items.values()
        if items:
            for item in items:
                msg += get_line(item.get_description())
            msg += get_line(get_splitter(self.__width))
            return msg
        else: 
            return self.__get_empty_msg()
    
    def __get_empty_msg(self) -> str: return "SHOPPING CART IS EMPTY".center(self.__width, "_")