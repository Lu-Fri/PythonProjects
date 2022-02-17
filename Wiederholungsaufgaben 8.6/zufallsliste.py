#! /usr/bin/env python3

from random import randint
lst = [ randint(0, 10) for _ in list(range(50)) ]

sum = 0
cnt = 0

for itm in lst:
    sum += itm

for itm in lst:
    if itm==0:
        cnt+=1

if cnt:
    for i in range(len(lst)):
        if lst[i]==0:
            print('Position der ersten Null:', i)
            break

else:
    print('Die Liste enthält keine Null.')