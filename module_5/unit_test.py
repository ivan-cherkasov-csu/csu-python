from unittest import TestCase, main
from input_util import get_user_input, str2number
from rainfall_data import collect_data, average
from bookstore import get_bonus_points

class Test(TestCase):
    
    def test_given_correct_input_can_get_value_from_user_input(self):
        values = ["1.1", "1"]
        source = lambda s: values.pop()
        self.assertEqual(get_user_input("", source, int), 1)
        self.assertAlmostEqual(get_user_input("", source, float), 1.1)
        
    def test_given_incorrect_input_get_user_input_prompts_until_input_is_correct(self):
        values = ["1", "","-1","", "1.1"]
        source = lambda s: values.pop()
        self.assertEqual(get_user_input("", source, str2number), 1)
        
    def test_given_correct_input_collect_data_returns_result(self):
        values = ["1.1","1.1","1.1","1.1","1.1","1.1","1.1","1.1","1.1","1.1","1.1","1.1","1.1","1"]
        source = lambda s: values.pop()
        years, months = collect_data(source)
        self.assertEqual(years, 1)
        self.assertEqual(len(months), 12)
        for month in months:
            self.assertAlmostEqual(month, 1.1)
        self.assertAlmostEqual(average(months), 1.1)
        
    def test_given_correct_input_bookstore_get_bonus_points_returns_result(self):
        values = ["0","1","2","3","4","5","6","7","8","9"]
        source = lambda s: values.pop()
        self.assertEqual(get_bonus_points(source), 60)
        self.assertEqual(get_bonus_points(source), 60)
        self.assertEqual(get_bonus_points(source), 30)
        self.assertEqual(get_bonus_points(source), 30)
        self.assertEqual(get_bonus_points(source), 15)
        self.assertEqual(get_bonus_points(source), 15)
        self.assertEqual(get_bonus_points(source), 5)
        self.assertEqual(get_bonus_points(source), 5)
        self.assertEqual(get_bonus_points(source), 0)
        self.assertEqual(get_bonus_points(source), 0)
               
if __name__ == '__main__':
    main()       
