import sys
import math_parse


def fail(): print("Cannot parse expression, incorrect input")
     
def calc(expr):
    if math_parse.check_support(["*","/"], expr):
        result = math_parse.parse_input(expr)
        if result is None:
            fail()
        else:
            print("answer: {} = {}".format(expr, result))
    else:
        fail()

if __name__ == '__main__':
    print("Hello, this is a program calculates result of multiplication and division of two numbers.")
    print("input your math expression or '--help' to get help on supported expressions, or 'exit' to exit program")
    expr = ""
    while True:
        expr = input().lower()
        if expr == 'exit': sys.exit()
        if expr == "--help":
            print("enter your expression in format <number> '*' or '/' <number>")
            print("you can use positive and negative numbers with decimal fraction")
            print("and '_' in large numbers e.g. 1_000_000")
            print("whitespaces are insignificant unless they split number in two parts")
            print("NOTE: division by 0 e.g. '1/0' will fail as incorrect input")
            print("examples:")
            print("2*2")
            print("-3.7 / -.3")
        else:
            calc(expr)