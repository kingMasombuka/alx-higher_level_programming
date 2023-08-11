

import sys
from itertools import islice


def execute_code():
    argv = sys.argv
    argcount = len(argv) - 1
    if argcount == 0:
        print(argcount)
    else:
        for i, arg in islice(enumerate(argv), 1, None):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    execute_code()
