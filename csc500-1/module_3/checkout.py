import math 
import sys
import os

def parse(input: str):
    try: 
        x = float(input)
        return x if x > 0 else None 
    except: return None

def parse_line(line: str):
    try:
        name, price = line.split("=")
        p = parse(price)  
        if p is None:
            return None
        else:
            return (name, p)
    except: return None

def round_currency(value: float):
    rnd = round(value, 2)
    diff = value - rnd
    if diff < 0 or math.isclose(diff, 0):
        return rnd
    else:
        return rnd + 0.01
    
def process_input(line:str, meals: dict):
    kv_pair = parse_line(line)
    if kv_pair is None:
        print("Can't parse input please try again")
    else:  
        if kv_pair in meals:
            meals[kv_pair] = meals[kv_pair] + 1
        else:
            meals[kv_pair] = 1
    
def calc_total(meals: dict):
    total = 0
    for name, price in meals:
        times = meals[(name, price)]
        total += round_currency(price * times)
        print("{}: {} x {}".format(name, price, times))
    tax = round_currency(total * 0.07)
    tips = round_currency(total * 0.18)
    return {"Subtotal": total, "Tax": tax, "Total": total+tax, "Tips": tips, "Balance Due": total + tax + tips}

if __name__ == '__main__':
    os.system("cls")
    print("Hello and welcome, to our restaurant checkout program.")
    print("Please input the cost of your meals one by one, name then price separated with '=' e.g. 'Soup=3.50'")
    print("Enter the empty line to get to the summary")
    meals = {}
    while True:
        item = input("> ")
        if item:
           process_input(item, meals)
        else:
            summary = calc_total(meals)
            print("________________________________")
            for key in summary:
                print("{}: {}".format(key, summary[key]))
            sys.exit()
            