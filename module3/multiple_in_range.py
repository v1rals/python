#! /usr/bin/python3
def multiple_in_range(min,max):
    lst = []
    _range = [i for i in range(min, max+1)]
    for value in _range:
        if value % 7 == 0 and value % 5 != 0:
            lst.append(value)
    return lst