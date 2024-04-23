import math

def dzielniki_wlasciwe(liczba):
    if liczba == 1:
        return []
    dzielniki = [1]
    for x in range(2,math.floor(liczba/2)+2):
        if liczba%x == 0:
            dzielniki.append(x)
    return dzielniki

def zaprzyjaznione(n):
    dzielniki = {}
    przyjaciele = []
    if n == 1:
        return None
    for x in range(1,n+1):
        dzielniki[x]=sum(dzielniki_wlasciwe(x))
    for liczba in dzielniki:
        liczba2 = dzielniki[liczba]
        if liczba != liczba2:
            if 1 < liczba2 < n:
                if liczba == dzielniki[liczba2]:
                    if (liczba2, liczba) not in przyjaciele:
                        przyjaciele.append((liczba,liczba2))
    return len(przyjaciele)


print('\n')
print(zaprzyjaznione(10000))