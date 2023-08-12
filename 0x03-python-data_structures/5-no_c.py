#!/usr/bin/python3

def no_c(my_string):
    to_list = list(my_string)
    new_list = [str(x) for x in to_list if x != "c" and x != "C" ]
    my_1string = ''.join(new_list)
    return my_1string
