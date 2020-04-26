#! /usr/bin/python3
def swap_max_and_min(lst= []):
    lst.sort()
    def getIndex(array):
        imin = array.index(min(array))
        imax = array.index(max(array))
        if imin > imax:
            return imin, imax
        return imax, imin
    lst[getIndex(lst)[0]], lst[getIndex(lst)[1]] = lst[getIndex(lst)[1]], lst[getIndex(lst)[0]]
    setlst = set(lst)
    if len(lst) == len(setlst):
        print("Все элементы уникальны,работает")
    else:
        print("Есть одинаковые элементы, невозможно выполнить условие")
        pass
    print(lst)
    return lst
swap_max_and_min([43,43,-50])