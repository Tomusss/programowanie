import math
import timeit

def Newton_rekurencja(n, k):
    if k == 0 or k == n:
        return 1
    return (Newton_rekurencja(n-1, k-1) + Newton_rekurencja(n-1, k))

def Newton_iteracja(n, k):
    tab = [1,1]
    '''
    1 1          
    1 2 1       0, 0+1, 1
    1 3 3 1     0, 0+1, 1+2, 2
    1 4 6 4 1   0, 0+1, 1+2, 2+3, 3
    [-1] -> [-1] + [-2]
    [-2] -> [-2] + [-3]
    [-3] -> [-3] + [-4]
        '''
    for x in range(1,n):
        dlugosc = len(tab)
        for y in range(dlugosc-1,0,-1):
            tab[y] = tab[y]+tab[y-1]
        tab.append(1)
    wynik = tab[k]
    return wynik

def Newton_silnia(n, k):
    wynik = math.factorial(n)/(math.factorial(n-k)*math.factorial(k))
    return int(wynik)
    
#print(Newton_rekurencja(7,5))
#print(Newton_iteracja(170,5))
#print(Newton_silnia(23,5))

'----------------mierzenie czasu----------------'

def rekurencja_czas():
    SETUP_CODE = '''
from __main__ import Newton_rekurencja'''
 
    TEST_CODE = '''
Newton_rekurencja(3,2)
'''

    time = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE)
 
    print('Newton_rekurencja(3,2): {}'.format(time))
 
    TEST_CODE2 = '''
Newton_rekurencja(10,4)
'''

    time2 = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE2)
 
    print('Newton_rekurencja(10,4): {}'.format(time2))

def iteracja_czas():
    SETUP_CODE = '''
from __main__ import Newton_iteracja'''
 
    TEST_CODE = '''
Newton_iteracja(3,2)
'''

    time = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE)
 
    print('Newton_iteracja(3,2): {}'.format(time))
 
    TEST_CODE2 = '''
Newton_iteracja(10,4)
'''

    time2 = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE2)
 
    print('Newton_iteracja(10,4): {}'.format(time2))

def silnia_czas():
    SETUP_CODE = '''
from __main__ import Newton_silnia'''
 
    TEST_CODE = '''
Newton_silnia(3,2)
'''

    time = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE)
 
    print('Newton_silnia(3,2): {}'.format(time))
 
    TEST_CODE2 = '''
Newton_silnia(10,4)
'''

    time2 = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_CODE2)
 
    print('Newton_silnia(10,4): {}'.format(time2))
 
 
#rekurencja_czas()
#iteracja_czas()
silnia_czas()