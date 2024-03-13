import math
import random
from time import perf_counter
from itertools import repeat
import gc
import matplotlib.pyplot as plt

def zmierz_raz(f, min_time=0.01):
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

def min1(lista):
    if lista:
        kandydat = lista[0]
        for element in lista:
            if element < kandydat:
                kandydat = element
        return kandydat
    
def min2(lista):
    if lista:
        kandydat = lista[0]
        for element in lista[1:]:
            if element < kandydat:
                kandydat = element
        return kandydat
    
def min3(lista):
    n = len(lista)
    if n > 0:
        kandydat = lista[0]
        i = 1
        while i<n:
            if lista[i] < kandydat:
                kandydat = lista[i]
            i += 1
        return kandydat

def min4(lista):
    if lista:
        lista = iter(lista)
        kandydat = next(lista)
        for element in lista:
            if element < kandydat:
                kandydat = element
        return kandydat

def wykres():
    dlugosci = [n for n in range(1,101)]
    czasy1 = []
    czasy2 = []
    czasy3 = []
    czasy4 = []
    for n in dlugosci:
        lista = [random.randint(1,1000) for x in range(1,n)]
        czasy1.append(zmierz_raz(lambda: min1(lista)))
        czasy2.append(zmierz_raz(lambda: min2(lista)))
        czasy3.append(zmierz_raz(lambda: min3(lista)))
        czasy4.append(zmierz_raz(lambda: min4(lista)))
    plt.plot(dlugosci, czasy1, label="min1")
    plt.plot(dlugosci, czasy2, label="min2")
    plt.plot(dlugosci, czasy3, label="min3")
    plt.plot(dlugosci, czasy4, label="min4")
    plt.xlabel("Długość listy")
    plt.ylabel("Czas działania (s)")
    plt.legend()
    plt.show()



def slowo(dlugosc_napisu):
    s = ''
    for x in range(dlugosc_napisu):
        a = random.randint(97,123) 
        s += chr(a)
    return s

def wykres_nap(dlugosc_napisu):
    dlugosci_listy = [n for n in range(1,101)]
    czasy1 = []
    czasy2 = []
    czasy3 = []
    czasy4 = []
    for n in dlugosci_listy:
        lista = [slowo(dlugosc_napisu) for x in range(1,n)]
        czasy1.append(zmierz_raz(lambda: min1(lista)))
        czasy2.append(zmierz_raz(lambda: min2(lista)))
        czasy3.append(zmierz_raz(lambda: min3(lista)))
        czasy4.append(zmierz_raz(lambda: min4(lista)))
    plt.plot(dlugosci_listy, czasy1, label="min1")
    plt.plot(dlugosci_listy, czasy2, label="min2")
    plt.plot(dlugosci_listy, czasy3, label="min3")
    plt.plot(dlugosci_listy, czasy4, label="min4")
    plt.xlabel("Długość listy")
    plt.ylabel("Czas działania (s)")
    plt.legend()
    plt.show()

def wykres_d():
    czasy1 = []
    czasy2 = []
    czasy3 = []
    czasy4 = []
    dlugosci_listy = []
    for n in range(1,101):
        dlugosci_listy.append(n)
        lista = [slowo(n) for x in range(1,1001)]
        czasy1.append(zmierz_raz(lambda: min1(lista)))
        czasy2.append(zmierz_raz(lambda: min2(lista)))
        czasy3.append(zmierz_raz(lambda: min3(lista)))
        czasy4.append(zmierz_raz(lambda: min4(lista)))
    plt.plot(dlugosci_listy, czasy1, label="min1")
    plt.plot(dlugosci_listy, czasy2, label="min2")
    plt.plot(dlugosci_listy, czasy3, label="min3")
    plt.plot(dlugosci_listy, czasy4, label="min4")
    plt.xlabel("Długość napisu")
    plt.ylabel("Czas działania (s)")
    plt.legend()
    plt.show()
wykres()
wykres_nap(1)
wykres_nap(32)
wykres_nap(1024)
wykres_d()
