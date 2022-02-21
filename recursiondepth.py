# Beispiel für unkontrollierte Rekursion
def f(n):
    # Vorsicht, unkontrollierte Rekursion
    return 1 + f(n)

f(2)