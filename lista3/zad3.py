import math
from time import perf_counter
from itertools import repeat
import gc
import matplotlib.pyplot as plt

def zmierz_raz(f, min_time=0.2):
    czas = 0
    ile_razy = 0
    ile_teraz = 1
    stan_gc = gc.isenabled()
    gc.disable()
    while czas < min_time:
        if ile_teraz == 1:
            start = perf_counter()
            f()
            stop = perf_counter()
        else:
            iterator = repeat(None, ile_teraz)
            start = perf_counter()
            for _ in iterator:
                f()
            stop = perf_counter()
        czas = stop-start
        ile_teraz *= 2
    if stan_gc:
        gc.enable()
    return czas/ile_teraz

def sito_sundarama(n):
    if n == 1:
        return []
    k = math.floor((n-2)/2 + 1)
    lista = [x for x in range(0,k)]
    pierwsze = []


    for i in range(1,k):
        for j in range(1,k):
            if i+j+2*i*j >= k:
                break
            lista[i+j+2*i*j] = None
        
    for x in range(0,k):
        if lista[x]:
            lista[x] = lista[x]*2 + 1
        if lista[x] != None:
            pierwsze.append(lista[x])

    pierwsze[0] = 2   

    return pierwsze

def sito_sundarama2(n):
    if n == 1:
        return []
    k = math.floor((n-2)/2 + 1)
    lista = [x for x in range(0,k)]
    pierwsze = []


    for i in range(1,math.floor((k-1)/3)+1):
        for j in range(1,math.floor((k+i) / (1+2*i))):
            lista[i+j+2*i*j] = None
        
    for x in range(0,k):
        if lista[x]:
            if lista[x]*2 + 1 == 9:
                print(lista)
            lista[x] = lista[x]*2 + 1
            
        if lista[x] != None:
            pierwsze.append(lista[x])

    pierwsze[0] = 2   

    return pierwsze

print(sito_sundarama2(100))

def pierwsze_sito(N):
    if N < 2:
        return []
    kandydaci = list(range(N))
    kandydaci[0] = None
    kandydaci[1] = None
    for x in kandydaci:
        if x is None:
            continue
        if x*x >= N:
            break
        for y in range(x*x, N, x):
            kandydaci[y] = None
    return [x for x in kandydaci if x is not None]

print('\n')
nki = [x for x in range(1,5)]
czasy1 = [zmierz_raz(lambda: sito_sundarama(2**x)) for x in range(1,5)]
czasy2 = [zmierz_raz(lambda: sito_sundarama2(2**x)) for x in range(1,5)]
czasy3 = [zmierz_raz(lambda: pierwsze_sito(2**x)) for x in range(1,5)]

plt.plot(nki, czasy1, label = "sito_sundarama")
plt.plot(nki, czasy2, label = 'sito_sundarama2')
plt.plot(nki, czasy3, label = 'sito_eratostenesa')

plt.xlabel('n')
plt.ylabel('Czas')

plt.legend()

plt.show()