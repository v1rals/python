#! /usr/bin/python3
def lists_2_dict(keys, values):
    dictionary = dict(zip(keys, values))
    print(dictionary)
    return dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
