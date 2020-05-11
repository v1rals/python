#! /usr/bin/python3
def swap_max_and_min(lst=None):
    if not lst:
        lst = []

    def getIndex(array):
        imin = array.index(min(array))
        imax = array.index(max(array))
        if imin > imax:
            return imin, imax
        return imax, imin
    lst[getIndex(lst)[0]], lst[getIndex(lst)[1]] = lst[getIndex(lst)[1]], lst[getIndex(lst)[0]]
    setlst = set(lst)
    if len(lst) != len(setlst):
        raise ValueError
    return lst
