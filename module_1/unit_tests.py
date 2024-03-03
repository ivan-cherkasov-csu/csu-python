import unittest
import math_parse

class TestParseMethods(unittest.TestCase):
    
    def test_parse_number_can_parse_int(self):
        self.assertEqual(math_parse.parse_number("5 "), 5)
        self.assertEqual(math_parse.parse_number(" -5"), -5)
    
    def test_parse_number_can_parse_float(self):
        self.assertAlmostEqual(math_parse.parse_number("0.5"), 0.5)
        self.assertAlmostEqual(math_parse.parse_number("2.0 "), 2.0)
        self.assertAlmostEqual(math_parse.parse_number("-0.5"), -0.5)

    def test_parse_op_name_can_parse_basic_math_operators(self):
        ops = ["+", "-", "*", "/"]
        for op in ops:
            self.assertIsNotNone(math_parse.parse_op_name(op))

    def test_parse_op_name_returns_none_for_incorrect_input(self):
        self.assertIsNone(math_parse.parse_op_name("a"))

    def test_parse_input_returns_correct_value_for_correct_input(self):
        self.assertEqual(math_parse.parse_input("2+2"), 4)
        self.assertEqual(math_parse.parse_input("2 - 2"), 0)
        self.assertEqual(math_parse.parse_input("2 *2"), 4)
        self.assertEqual(math_parse.parse_input("2/ 2"), 1)
        self.assertEqual(math_parse.parse_input("-2+-2"), -4)
        self.assertEqual(math_parse.parse_input("2+.2"), 2.2)
        self.assertAlmostEqual(math_parse.parse_input("-3.7--.3"), -3.4)
        self.assertAlmostEqual(math_parse.parse_input("-3.7 - -.3"), -3.4)
        self.assertAlmostEqual(math_parse.parse_input("-3.7 - -0.3"), -3.4)
        self.assertEqual(math_parse.parse_input("2_000_000 + 2_000_000"), 4_000_000)
        self.assertAlmostEqual(round(math_parse.parse_input("-3.7 / -0.3"), 4), 12.3333)  

    def test_parse_input_returns_correct_value_for_incorrect_input(self):
        self.assertIsNone(math_parse.parse_input("2+a"))
        self.assertIsNone(math_parse.parse_input("- 2"))
        self.assertIsNone(math_parse.parse_input("x *y"))
        self.assertIsNone(math_parse.parse_input("2.a/ 2"))
        self.assertIsNone(math_parse.parse_input("2/0")) 

if __name__ == '__main__':
    unittest.main()