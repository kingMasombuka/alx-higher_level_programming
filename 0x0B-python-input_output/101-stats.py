#!/usr/bin/python3
"""Reads  input and computes metrics.

"""


def print_stats(size, status_codes):
    """Print  metrics.

    Args:
        status_codes (dict): The  count of status codes.
        size (int): The  read file size.
    """
    print("File size: {}".format(size))
    for keys in sorted(status_codes):
        print("{}: {}".format(keys, status_codes[keys]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    counter = 0

    try:
        for line in sys.stdin:
            if counter == 10:
                print_stats(size, status_codes)
                counter = 1
            else:
                counter += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
