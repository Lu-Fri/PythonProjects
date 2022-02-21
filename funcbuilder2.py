import math
def verschachteln(f, g, x):
    return f(g(x))

verschachteln(print, math.sin, 0.2)
print(math.sin(0.2))

ergebnis = verschachteln(math.sin, math.sqrt, 0.5)
print(ergebnis == math.sin(math.sqrt(0.5)))