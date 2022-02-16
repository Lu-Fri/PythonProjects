#!/usr/bin/env python3

sum = 0
for i in range(1, 1001):
    sum += i
"""
1.
sum = 0
i = 1
while i<=1000:
    sum += i

2.
from functools import reduce
sum = reduce(lambda x, y: x + y, list(range(1,1001)))

3.
sum = sum(i for i in range(1, 1001))
"""
print('Summe der Zahlen von 1 bis 1000: ', sum)
# Ergebnis: 500500
