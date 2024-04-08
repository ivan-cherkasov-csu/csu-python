import types
from os import system 
class Greeting(object):
    def hello(self) -> str: return "Hello, world!"
    
def format_as_money(value: float) -> str: f"${value:.2f}"
    
if __name__ == '__main__':  
    system("cls")
    p = 100
    s= format_as_money(p)
    print(s)
    print(f"{s:>18}")