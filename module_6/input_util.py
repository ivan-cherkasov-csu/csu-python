from typing import Callable

def str2number(value: str) -> int | None: 
    try: 
        q = int(value) 
        return q if q > 0 else None
    except: None
    
def str2uint(value: str) -> int | None: 
    try: 
        q = int(value) 
        return q if q > -1 else None
    except: None

def str2float(value: str) -> float | None:
        try: return float(value)
        except: None 
        
def get_user_input(prompt: str, source: Callable[[str],str], convert: Callable[[str],int|None] | Callable[[str],float|None]) -> int|float|None:
    while True:
        input = source(f"Enter the {prompt}: ")
        value = convert(input)
        if value is not None: return value
        else: print(f"Incorrect input {input} for {prompt}, please try again...")