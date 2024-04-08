from unittest import TestCase, main
from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
from StoreFront import StoreFront


class MockInput(object):
    __items: list[str]
    
    def __init__(self, incoming: list) -> None:
        items = []
        for i in incoming:
            items.append(str(i))
        items.reverse()
        self.__items = items
    
    def get_items(self, foo: str) -> str: return self.__items.pop() if self.__items else "q"
        
class Test(TestCase):
    
    def test_ItemToPurchase_can_print_description(self):
        item = ItemToPurchase("foo", 1, 0, "bar")
        self.assertEqual(f"foo -bar @ {'$1.00':>7}", item.get_description(0,0))
        
    def test_shopping_cart_can_add_item(self):
        item = ItemToPurchase("foo", 1, 5, "bar")
        cart = ShoppingCart()
        cart.add_item(item)
        self.assertEqual(5, cart.get_num_items_in_cart())
    
    def test_shopping_cart_can_remove_item_from_cart(self):
        item = ItemToPurchase("foo", 1, 5, "bar")
        cart = ShoppingCart()
        cart.add_item(item)
        self.assertEqual(5, cart.get_num_items_in_cart())
        cart.remove_item(item.item_name)
        self.assertEqual(0, cart.get_num_items_in_cart())
        
    def test_shopping_cart_cannot_remove_item_not_in_cart(self):
        item = ItemToPurchase("foo", 1, 5, "bar")
        cart = ShoppingCart()
        cart.add_item(item)
        self.assertEqual(5, cart.get_num_items_in_cart())
        cart.remove_item("bar")
        self.assertEqual(5, cart.get_num_items_in_cart())
        
    def test_shopping_cart_can_modify_item_in_cart(self):
        item = ItemToPurchase("foo", 1, 5, "bar")
        cart = ShoppingCart()
        cart.add_item(item)
        self.assertEqual(5, cart.get_num_items_in_cart())
        item.item_quantity = 10
        cart.modify_item(item)
        self.assertEqual(10, cart.get_num_items_in_cart())
        
    def test_shopping_cart_cannot_modify_item_not_in_cart(self):
        item = ItemToPurchase("foo", 1, 5, "bar")
        cart = ShoppingCart()
        cart.add_item(item)
        self.assertEqual(5, cart.get_num_items_in_cart())
        cart.modify_item(ItemToPurchase())
        self.assertEqual(5, cart.get_num_items_in_cart())
    
    def test_shopping_cart_can_get_cost(self):
        item = ItemToPurchase("foo",3.5, 5, "bar")
        cart = ShoppingCart()
        cart.add_item(item)
        self.assertEqual(17.5, cart.get_cost_of_cart())
        
    def test_store_front_can_quit(self):
        mock = MockInput(["i"])
        store = StoreFront(mock.get_items)
        cart = ShoppingCart()
        store.print_menu(cart)
        
    def test_store_front_can_add_item(self):
        mock = MockInput(["a", "Earbuds", 1])
        store = StoreFront(mock.get_items)
        cart = ShoppingCart()
        store.print_menu(cart)
        self.assertEqual(29.73, cart.get_cost_of_cart())
        
    def test_store_front_cannot_add_unavailable_item(self):
        mock = MockInput(["a", "foo", 1])
        store = StoreFront(mock.get_items)
        cart = ShoppingCart()
        store.print_menu(cart)
        self.assertEqual(0, cart.get_cost_of_cart())
        
    def test_store_front_can_modify_item(self):
        mock = MockInput(["a", "Earbuds", 1, "c", "Earbuds", 3])
        store = StoreFront(mock.get_items)
        cart = ShoppingCart()
        store.print_menu(cart)
        self.assertAlmostEqual(3*29.73, cart.get_cost_of_cart())
        
    def test_store_front_cam_remove_item(self):
        mock = MockInput(["a", "Earbuds", 1, "r", "Earbuds"])
        store = StoreFront(mock.get_items)
        cart = ShoppingCart()
        store.print_menu(cart)
        self.assertAlmostEqual(0, cart.get_cost_of_cart())
        
if __name__ == '__main__':
    main()    