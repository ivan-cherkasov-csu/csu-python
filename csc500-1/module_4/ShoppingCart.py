from typing import Callable, Dict
from ItemToPurchase import ItemToPurchase
import os

class ShoppingCart(object):
    __input_source: Callable[[str], str]
    __inputs: Dict[str, tuple[Callable[[str], str|float|int|None], Callable[[ItemToPurchase, str|float|int], None]]]
    __items: Dict[str, ItemToPurchase]
    def __init__(self, input_source: Callable[[str], str]) -> None:
        self.__input_source = input_source
        self.__items = {}
        self.__inputs = {"item name": (self.convert_str, self.__bind_name), 
                  "item price": (self.convert_float, self.__bind_price), 
                  "item quantity": (self.convert_int, self.__bind_quantity)}
    
    def fill_cart(self) -> Dict[str, ItemToPurchase]:
        while True:
            item = ItemToPurchase()
            for kv in self.__inputs.items():
                prompt = kv[0]
                convert = kv[1][0]
                bind = kv[1][1]
                value = self.parse_user_input(prompt, convert)
                if value is None: return self.__items
                else: bind(item, value)
            self.__items[item.item_name] = item #assume user replaces items then name is same
            
    def get_check(self) -> str:
        check: str = "TOTAL COST" + os.linesep
        total: float = 0
        items = self.__items.values()
        for item in items:
            check += item.print_item_cost() + os.linesep
            total += item.total()
        return check + f"Total:{total}" 
            
    def parse_user_input(self, prompt: str, convert: Callable[[str], str|float|int|None]) -> str|float|int|None:
        while True:
            input = self.__check_for_exit_command(self.__input_source(f"Enter the {prompt}: "))
            if input is None: return input
            value = convert(input)
            if value is not None: return value
            print(f"Cannot parse {prompt}={input}, please try again...")
            
    def convert_str(self, value: str) -> str: return value.strip()
    def convert_int(self, value: str) -> int | None: 
        try: 
            q = int(value) 
            return q if q > 0 else None
        except: None
    def convert_float(self, value: str) -> float | None:
        try: return float(value)
        except: None 
            
    def __check_for_exit_command(self, input: str) -> str | None: return input if input and input.lower() != "exit" else None
    def __bind_name(self, item: ItemToPurchase, value: str) -> None: item.item_name = value
    def __bind_quantity(self, item: ItemToPurchase, value: int) -> None: item.item_quantity=value
    def __bind_price(self, item: ItemToPurchase, value: float) -> None: item.item_price = value