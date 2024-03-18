from typing import Callable
from input_util import get_user_input, str2uint

def get_bonus_points(source: Callable[[str], str]) -> int:
    number_of_books = get_user_input("how many books did you purchased this month", source, str2uint)
    if number_of_books < 2: return 0
    if number_of_books < 4: return 5
    if number_of_books < 6: return 15
    if number_of_books < 8: return 30
    return 60