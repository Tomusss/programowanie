import math

def dzielniki_wlasciwe(liczba):
    if liczba == 1:
        return []
    dzielniki = [1]
    for x in range(2,math.floor(liczba/2)+2):
        if liczba%x == 0:
            dzielniki.append(x)
    return dzielniki

def doskonala(liczba):
    suma = 0
    for l in dzielniki_wlasciwe(liczba):
        suma += l
    if suma == liczba:
        return liczba

def liczby_doskonale(n):
    doskonale = []
    for liczba in range(2,n+1):
        if doskonala(liczba):
            doskonale.append(liczba)
    return doskonale
print('\n')
print(liczby_doskonale(100))