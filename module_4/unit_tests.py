import unittest
import os
from  ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

class TestShoppingList(unittest.TestCase):

    def test_can_create_item_to_purchase(self):
        item = ItemToPurchase()
        self.assertEqual(item.item_name, "none")
        self.assertAlmostEqual(item.item_price, 0)
        self.assertEqual(item.item_quantity, 0)
        self.assertEqual(item.print_item_cost(), "none 0 @ $0 = $0")
    
    def test_given_correct_input_shopping_cart_can_parse_user_input(self):
        name = "Foo"
        price = 5.5
        qty = 100
        mock = [str(qty), str(price), "Foo"]
        cart = ShoppingCart(lambda s: mock.pop())
        self.assertEqual(cart.parse_user_input("Name", cart.convert_str), name)
        self.assertAlmostEqual(cart.parse_user_input("Price", cart.convert_float), price)
        self.assertEqual(cart.parse_user_input("Qty", cart.convert_int), qty)
    
    def test_given_input_match_exit_condition_shopping_cart_can_parse_user_input_returns_none(self):
        cart = ShoppingCart(lambda s: ["ExIt", None].pop())
        boom = lambda: 1/0
        self.assertEqual(cart.parse_user_input(None, boom), None)
        self.assertEqual(cart.parse_user_input(None, boom), None)
    
    def test_given_no_input_shopping_cart_can_get_check(self):
        cart = ShoppingCart(lambda s: None)
        self.assertEqual(cart.get_check(), "TOTAL COST" + os.linesep + "Total:0")
        
    def test_given_correct_input_can_fill_shopping_cart(self):
        foo = ItemToPurchase.create("Foo", 5.5, 100)
        bar = ItemToPurchase.create("Bar", 2.06, 2)
        mock = ["exit", str(bar.item_quantity), str(bar.item_price), bar.item_name, str(foo.item_quantity), str(foo.item_price), foo.item_name]
        cart = ShoppingCart(lambda s: mock.pop())
        result = cart.fill_cart()
        self.assertIn(foo.item_name, result)
        self.assertEqual(foo.item_name, result[foo.item_name].item_name)
        self.assertAlmostEqual(foo.item_price, result[foo.item_name].item_price)
        self.assertEqual(foo.item_quantity, result[foo.item_name].item_quantity)
        self.assertIn(bar.item_name, result)
        self.assertEqual(bar.item_name, result[bar.item_name].item_name)
        self.assertAlmostEqual(bar.item_price, result[bar.item_name].item_price)
        self.assertEqual(bar.item_quantity, result[bar.item_name].item_quantity)
        
    def test_given_correct_input_shopping_cart_can_get_check(self):
        foo = ItemToPurchase.create("Foo", 5.5, 100)
        bar = ItemToPurchase.create("Bar", 2.06, 2)
        mock = ["exit", str(bar.item_quantity), str(bar.item_price), bar.item_name, str(foo.item_quantity), str(foo.item_price), foo.item_name]
        cart = ShoppingCart(lambda s: mock.pop())
        cart.fill_cart()
        result = cart.get_check()
        self.assertEqual(result, f"TOTAL COST{os.linesep}Foo 100 @ $5.5 = $550.0{os.linesep}Bar 2 @ $2.06 = $4.12{os.linesep}Total:554.12")
        
 
if __name__ == '__main__':
    unittest.main()