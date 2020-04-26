#! /usr/bin/python3
def dict_swap(swap):
    swapped = dict(reversed(item) for item in swap.items())
    print(swap)
    print(swapped)
    return swapped
swap = {
       'Name': 'John',
       'Age': 44,
       'JobTitle': "DevOps"
}
dict_swap(swap)