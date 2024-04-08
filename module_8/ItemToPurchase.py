from input_util import format_as_money

class ItemToPurchase(object):
    item_name: str
    item_price: float
    item_quantity: int
    item_description: str

    def __init__(self, name: str = "none", price: float = 0, qty: int = 0, description: str = "") -> None:
        self.item_name = name
        self.item_price = price
        self.item_quantity = qty
        self.item_description = description
       
    def total(self) -> float: return self.item_price * self.item_quantity

    def print_item_cost(self) -> str: return str(self)
    
    def get_description(self, namePadding: int = 16, descPadding: int = 40) -> str: 
        return f"{self.item_name:<{namePadding}} -{self.item_description:<{descPadding}} @ {format_as_money(self.item_price):>7}"
         
    def __str__(self) -> str:
        return f"{self.item_name} {self.item_quantity} @ {format_as_money(self.item_price)} = {format_as_money(self.total())}"
    
    def __bool__(self) -> bool: return True if self.item_quantity or self.item_price or self.item_name != "none" else False 