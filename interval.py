#! /usr/bin/python3
import sys

x = int(sys.argv[1])
if x >= 19 or 17 > x > 14 or -15 < x <= 12:
        print ("True")
else:
        print("False")