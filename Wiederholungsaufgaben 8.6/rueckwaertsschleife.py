#! /usr/bin/env python3

min = 125.0
max = 160.0
nmax = 11
delta = (max - min) / (nmax - 1)

for i in range(nmax):
    x = min + delta *i
    print(x)