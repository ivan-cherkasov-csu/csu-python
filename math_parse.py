def add(a, b): return a+b
def sub(a, b): return a-b
def mul(a, b): return a*b
def div(a, b): 
    if b == 0:
        return None
    return a/b

def parse_int(num_string):
    try: return int(num_string)
    except: return None

def parse_float(num_string):
    try: return float(num_string)
    except: return None

def parse_number(num_string):
    i = parse_int(num_string)
    return parse_float(num_string) if i is None else i 

def parse_op_name(op_name):
    ops = { "*": mul, "/": div,"+": add, "-": sub}
    return ops[op_name] if op_name in ops else None

def parse_input(input_str):
    ops = ["*", "/", "+", "-"]
    input_str = input_str.lstrip()
    rem_sign = input_str.lstrip("-").lstrip("+")
    offset = len(input_str) - len(rem_sign)
    for op in ops:
        pos = rem_sign.find(op)
        if pos > -1:
            pos += offset
            func = parse_op_name(op)
            left = parse_number(input_str[:pos].strip())
            right = parse_number(input_str[pos+1:].strip())
            return None if left is None or right is None else func(left, right)
    return None

def check_support(operations, expr):
    for op in operations:
        if expr.find(op)>-1:
            return True
    return False 