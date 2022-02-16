#!/usr/bin/env python3

jahr = int(input('Geben Sie das aktuelle Jahr an: ')) # Ist dieses Jahr ein Schaltjahr?

if jahr % 400 == 0:
    schaltjahr = True
elif jahr % 100 == 0:
    schaltjahr = False
elif jahr % 4 == 0:
    schaltjahr = True
else:
    schaltjahr = False

if schaltjahr:
    print(jahr, 'ist ein Schaltjahr.')
else:
    print(jahr, 'ist kein Schaltjahr.')
