class ItemToPurchase(object):
    item_name: str
    item_price: float
    item_quantity: int

    def __init__(self) -> None:
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
    @classmethod
    def create(cls, name: str, price: float, quantity: int) -> "ItemToPurchase":
        item = cls()
        item.item_name = name
        item.item_price = price
        item.item_quantity = quantity
        return item
         
    def __str__(self) -> str:
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.total()}"
       
    def total(self) -> float: return self.item_price * self.item_quantity

    def print_item_cost(self)-> str: return str(self)