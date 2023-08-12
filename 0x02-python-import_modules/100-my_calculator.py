##!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import calculator_1 as cal

    argv = sys.argv
    argcount = len(argv) - 1
    if argcount != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    print(argv)
    print(argcount)