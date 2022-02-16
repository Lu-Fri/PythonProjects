#!/usr/bin/env python3

print('In Python gibt es verschiedene Datentypen!')
objekt = input('Gib einen Datentyp an: ')

if objekt == 'int' or objekt == 'integer':
    print('x=3')
elif objekt == 'float' or objekt == 'floating-point number':
    print('x=3.0')
elif objekt == 'complex' or objekt == 'complex number':
    print('x=3+4j')
elif objekt == 'bool' or objekt == 'boolean value':
    print('x=bool(1)')
elif objekt == 'str' or objekt == 'string':
    print('`x=abc`')
elif objekt == 'tupel' or objekt == 'tuple':
    print('x=(1, 2, 3)')
elif objekt == 'list' or objekt == 'Liste':
    print('x=[1, 2, 3]')
elif objekt == 'set' or objekt == 'Set':
    print('x={1, 2, 3}')
elif objekt == 'dict' or objekt == 'dictionary':
    print('x={1:`rot`, 2:`blau`}')
elif objekt == 'bytearray' or objekt == 'Byte-Array':
    print('x=bytearray(...)')
elif objekt == 'io.TextIOWrapper' or objekt == 'Dateien':
    print('x=open(`readme.tyt`)')
else:
    print('Das war wohl keine richtige Eingabe :/')
