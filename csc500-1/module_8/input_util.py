import os

def str2number(value: str) -> int | None: 
    try: 
        q = int(value) 
        return q if q > 0 else None
    except: None
    
def format_as_money(value: float) -> str: return f"${value:.2f}"

def get_splitter(length: int, char: str = "-") -> str: return "".center(length, char)

def get_line(string: str) -> str: return string + os.linesep