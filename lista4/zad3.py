import random

def sortowanie_zliczanie(lista, k, klucze = list(range(10))):
    pozycje = {}
    wystąpienia = {}
    
    for x in klucze:
        wystąpienia[x] = 0
    for elem in lista:
        if len(str(elem)) >= k:
            wystąpienia[int(str(elem)[-k])] += 1
        else:
            wystąpienia[0] += 1
    for elem in klucze:
        if wystąpienia[elem] == 0:
            wystąpienia.__delitem__(elem)

    ile_wystapien = 0
    for elem in wystąpienia:
        pozycje[elem] = ile_wystapien
        ile_wystapien += wystąpienia[elem]

    postortowana = [0 for x in range(0,len(lista))]
    for elem in lista:
        if len(str(elem)) >= k:
            postortowana[pozycje[int(str(elem)[-k])]] = elem
            pozycje[int(str(elem)[-k])] += 1
        else:
            postortowana[pozycje[0]] = elem
            pozycje[0] += 1

    return postortowana

def sortowanie_pozycyjne(lista):
    cyfry_znaczace = len(str(max(lista)))
    for x in range(1,cyfry_znaczace + 1):
        lista = sortowanie_zliczanie(lista, x)
    return lista
print('-----------rozwiazanie-----------')
lista = [random.randint(1,10000) for x in range(10)]
print(lista,sortowanie_pozycyjne(lista))