##!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from itertools import islice
    argv = sys.argv
    argcount = len(argv) - 1
    if argcount == 0:
        print("{} arguments.".format(argcount))
    elif argcount == 1:
        print("{} argument:".format(argcount))
        print("{}: {}".format(argcount, argv[1]))
    else:
        print("{} arguments:".format(argcount))
        for i, arg in islice(enumerate(argv), 1, None):
            print("{}: {}".format(i, arg))
