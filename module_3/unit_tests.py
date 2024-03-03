import unittest
import checkout

class TestCheckout(unittest.TestCase):

    def test_round_currency_returns_correct_value(self):
        self.assertEqual(checkout.round_currency(1.234), 1.24)
        self.assertEqual(checkout.round_currency(1.000001), 1.01)
        self.assertEqual(checkout.round_currency(3.0975), 3.10)

    def test_given_input_correct_parse_returns_price(self):
        self.assertAlmostEqual(checkout.parse("10"), 10)
        self.assertAlmostEqual(checkout.parse("1.01"), 1.01)

    def test_given_input_incorrect_parse_returns_none(self):
        self.assertIsNone(checkout.parse("-10"))
        self.assertIsNone(checkout.parse("foo bar"))
        self.assertIsNone(checkout.parse("1e51-3"))

    def test_given_input_correct_parse_line_returns_name_value_pair(self):
        self.assertEqual(checkout.parse_line("Pizza=10.50"), ("Pizza", 10.5))
        self.assertEqual(checkout.parse_line("Steak=23.25"), ("Steak", 23.25))

    def test_given_correct_input_process_input_stores_values_in_dictionary(self):
        data = {}
        checkout.process_input("Pizza=10.50", data)
        checkout.process_input("Pizza=10.50", data)
        checkout.process_input("Steak=23.25", data)
        self.assertAlmostEqual(data[("Pizza", 10.5)], 2)
        self.assertAlmostEqual(data[("Steak", 23.25)], 1)

    def test_given_correct_input_calc_total_returns_correct_values(self):
        data = {}
        checkout.process_input("Pizza=10.50", data)
        checkout.process_input("Pizza=10.50", data)
        checkout.process_input("Steak=23.25", data)
        result = checkout.calc_total(data)
        sub = 10.5*2+23.25
        tax = checkout.round_currency(sub * 0.07)
        tips = checkout.round_currency(sub * 0.18)
        bal = sub + tax + tips
        self.assertAlmostEqual(result["Subtotal"], sub)
        self.assertAlmostEqual(result["Tax"], tax)
        self.assertAlmostEqual(result["Total"], tax+sub)
        self.assertAlmostEqual(result["Tips"], tips)
        self.assertAlmostEqual(result["Balance Due"], bal)

if __name__ == '__main__':
    unittest.main()