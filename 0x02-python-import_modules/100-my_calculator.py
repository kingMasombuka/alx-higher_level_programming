#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    argv = sys.argv
    argcount = len(argv) - 1
    operators = ["+", "*", "/", "-"]
    if argcount != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    try:
        a = int(argv[1])
        b = int(argv[3])
    except ValueError:
        print("Input Numbers only like : 1 ,2 ,3 ,4")
        sys.exit(1)
    if argv[2] == "+":
        print("{} {} {} = {}".format(a, argv[2], b, cal.add(a, b)))
    if argv[2] == "-":
        print("{} {} {} = {}".format(a, argv[2], b, cal.sub(a, b)))
    if argv[2] == "*":
        print("{} {} {} = {}".format(a, argv[2], b, cal.mul(a, b)))
    if argv[2] == "/":
        print("{} {} {} = {}".format(a, argv[2], b, cal.div(a, b)))
    sys.exit(0)
