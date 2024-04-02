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
print(Newton_silnia(23,5))

# compute binary search time
def rekurencja_czas():
    SETUP_CODE = '''
from __main__ import Newton_rekurencja'''
 
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
binary_search(mylist, find)'''
 
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)
 
    # printing minimum exec. time
    print('Binary search time: {}'.format(min(times)))
 
 
# compute linear search time
def linear_time():
    SETUP_CODE = '''
from __main__ import linear_search
from random import randint'''
 
    TEST_CODE = '''
mylist = [x for x in range(10000)]
find = randint(0, len(mylist))
linear_search(mylist, find)
    '''
    # timeit.repeat statement
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=10000)
 
    # printing minimum exec. time
    print('Linear search time: {}'.format(min(times)))
 
 
if __name__ == "__main__":
    linear_time()
    binary_time()