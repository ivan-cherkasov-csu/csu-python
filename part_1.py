import sys
import math_parse

def fail(): print("Cannot parse expression, incorrect input")
     
def calc(expr):
    if math_parse.check_support(["+","-"], expr):
        result = math_parse.parse_input(expr)
        if result is None:
            fail()
        else:
            print("answer: {} = {}".format(expr, result))
    else:
        fail()

if __name__ == '__main__':
    print("Hello, this is a program calulates result of addition and subtraction of two numbers.")
    print("input your math expression or '--help' to get help on supported expressions, or 'exit' to exit program")
    expr = ""
    while True:
        expr = input().lower()
        if expr == 'exit': sys.exit()
        if expr == "--help":
            print("enter your expression in format <number> '+' or '-' <number>")
            print("you can use positive and negative numbers with decimal fraction")
            print("and '_' in large numbers e.g. 1_000_000")
            print("whitespaces are insignificant unless they split number in two parts")
            print("examples:")
            print("2+2")
            print("-3.7 - -.3")
        else:
            calc(expr)