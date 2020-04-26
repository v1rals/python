#! /usr/bin/python3
def bold(f):
    return lambda: "<b>" + f() + "</b>"
def italic(f):
    return lambda: "<i>" + f() + "</i>"
def underline(f):
    return lambda: "<u>" + f() + "</u>"

@bold
@italic
@underline
def say():
    return "Hello"

print(say())
