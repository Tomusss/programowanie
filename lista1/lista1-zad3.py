import numpy as np
import random

# GENEROWANIE LOSOWEJ MACIERZY
rz = random.randint(2,6)
kol = random.randint(2,6)
mac = np.random.randint(0,1000,size =(rz,kol))
print(mac)

def sasiedztwo(A, r, i, j):
    y, x = A.shape
    #wyliczenie rz/kol
    d = i - r
    g = i + r + 1
    p = j + r + 1
    l = j - r
    if l < 0:
        l = 0
    if p > x:
        p = x
    if d < 0:
        d = 0
    if g > y:
        g = y
    indeksy_wierszy = [x for x in range(d,g)]
    indeksy_kolumn = [x for x in range(l,p)]
    wycinek = np.take(A, indeksy_wierszy, axis=0)  
    wycinek = np.take(wycinek, indeksy_kolumn, axis=1)  
    return wycinek

print(sasiedztwo(mac,1,1,2))

def znajdz(A,w):
    miejsca = []
    k = A[0][0]
    i, j = A.shape
    for x in range(0,j):
        for z in range(0,i):
            if A[z][x] > w:
                return 0
    return 1       

def maksima_lokalne(A):
    maksima = []
    i,j = A.shape
    for x in range(0,j):
        for y in range(0,i):
            otoczenie = sasiedztwo(A,1,x,y)
            wart = A[y][x]
            if znajdz(otoczenie,wart):
                maksima.append((y,x))
    return  maksima
#print(maksima_lokalne(mac))

def czy_jednomodalna(A):
    if len(maksima_lokalne(A)) == 1:
        return True
    else:
        return False
#print(czy_jednomodalna(mac))