
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    my_new_list = my_list[:]
    for idx, x in enumerate(my_new_list):
        if x == search:
            my_new_list[idx] = replace
    return my_new_list
