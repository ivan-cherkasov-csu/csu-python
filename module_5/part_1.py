from rainfall_data import collect_data, average
from os import system

def singular_or_plural(years: int) ->str: "years" if years > 1 else "year"

if __name__ == '__main__':  
    system("cls")
    years, data = collect_data(input)
    result = average(data)
    print(f"The average rainfall level for period of {years} {singular_or_plural(years)} is {result}.")
    