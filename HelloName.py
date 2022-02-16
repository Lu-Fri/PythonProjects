#!/usr/bin/env python3
# Beispieldatei Hello.py
import time, locale
name = input('Geben Sie Ihren Namen an: ')
print('Hallo %s!' % name)

# Datum und Zeit in aktueller Lokalisierung
locale.setlocale(locale.LC_ALL, '')
time = time.strftime('Heute ist %A, der %d. %B.')
print(time)
