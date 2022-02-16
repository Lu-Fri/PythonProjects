#!/usr/bin/env python3

import sys
if(len(sys.argv)<=1):
    print('Es wurden keine Parameter übergeben.')
else:
    for x in sys.argv[1:]:
        print('Parameter:', x)

"""
./parameter.py -x -y readme.txt *.txt
Parameter: -x
Parameter: -y
Parameter: readme.txt
"""
