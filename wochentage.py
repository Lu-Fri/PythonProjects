#!/usr/bin/env python3
# Beispieldatei Wochentage.py
alletage = { 1: 'Montag', 2: 'Dienstag', 3: 'Mittwoch', 4: 'Donnerstag', 5: 'Freitag', 6: 'Samstag', 7: 'Sonntag'}

tag = 6

if tag in alletage:
    s = alletage[tag]
else:
    s = 'ungültig'
print('Wochentag:', s)
