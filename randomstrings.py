from random import randint
from string import ascii_lowercase
from random import choices

def randomstr(n):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    max = len(letters)
    lst = [letters[randint(0, max-1)] for _ in range(n)]
    return ''.join(lst)

def randomstr2(n):
    return ''.join(choices(ascii_lowercase, k=n))

print(randomstr(4))
print(randomstr2(8))