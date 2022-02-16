#!/usr/bin/env python3

jahr = int(input('Geben Sie das aktuelle Jahr an: ')) # Ist dieses Jahr ein Schaltjahr?
monat = int(input('Der wievielte Monat soll bestimmt werden?: '))

if jahr % 400 == 0:
    schaltjahr = True
elif jahr % 100 == 0:
    schaltjahr = False
elif jahr % 4 == 0:
    schaltjahr = True
else:
    schaltjahr = False

if monat in (1, 3, 5, 7, 8, 10, 12): #todo: Mein code
    tage = 31
elif monat in (4, 6, 9, 11):
    tage = 30
elif schaltjahr == True:  #elif monat ==2:
    tage = 29             #    tage = 28 if schaltjahr else 29
elif schaltjahr == False: #else:
    tage = 28             #    print('Ungültiger Monat!')
else:                     #tage = 0
    print('Fehler bei Tagen!')

if schaltjahr:
    print(jahr, 'ist ein Schaltjahr.')
else:
    print(jahr, 'ist kein Schaltjahr.')

print('Der %d. Monat im Jahr %d hat %d Tage.'
      % (monat, jahr, tage))
