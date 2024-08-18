from typing import Callable 
from calendar import Month, month_name
from statistics import mean
from input_util import get_user_input, str2float, str2number
      
def collect_data(source: Callable[[str], str]) -> tuple[int, list[float]]:
    result = []
    years = get_user_input("number of years", source, str2number)
    i = 1
    while i <= years:
        for month in Month:
            result.append(get_user_input(f"rainfall level for {month_name[month]} of year {1}", source, str2float)) 
        i+=1           
    return (years, result)

def average(data: list) -> float: return mean(data)