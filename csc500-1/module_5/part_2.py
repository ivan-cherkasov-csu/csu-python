from bookstore import get_bonus_points
from os import system

if __name__ == '__main__':  
    system("cls")
    points = get_bonus_points(input)
    print(f"The number of bonus point you've earned this month is {points}.")