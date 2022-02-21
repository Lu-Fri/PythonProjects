import math

def funcbuilder(f, n):
    def newfunc(x):
        return f(n*x) # Ergebnis von newfunc
    return newfunc    # Ergebnis von funcbuilder

# bildet die Funktion sin(2*x)
f1 = funcbuilder(math.sin, 2)
print(f1(0.4), math.sin(0.4*2))

# bildet die Funktion cos(4*x)
f2 = funcbuilder(math.cos, 4)
print(f2(0.07), math.cos(0.07*4))

# def funcbuilder(f, n):
#   return lambda x: f(n*x)