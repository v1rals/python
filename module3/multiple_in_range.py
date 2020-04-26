#! /usr/bin/python3
def multiple_in_range(min,max):
    global range, value
    lst = []
    _range = [i for i in range(min, max+1)]
    print(_range)
    for value in _range:
        if value % 7 == 0 and value % 5 != 0:
            lst.append(value)
    print(lst)
    return lst

multiple_in_range(-77,-7)

multiple_in_range(-77,77)

multiple_in_range(7,77)