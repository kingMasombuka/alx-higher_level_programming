##!/usr/bin/python3


if __name__ == "__main__":
    import sys

    sum = 0
    argv = sys.argv
    argcount = len(argv) - 1
    for arg in argv[1:]:
        sum += int(arg)
    print(sum)
