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

def bisekcja(f, a, b, tolerancja=1e-6):
    c = (a+b)/2
    pół_długości = (b-a)/2
    if pół_długości <= tolerancja:
        return c
    f_a = f(a)
    while pół_długości > tolerancja:
        f_c = f(c)
        if f_a*f_c < 0:
            b = c
        elif f_a*f_c > 0:
            a = c
            f_a = f_c
        else:
            return c
        pół_długości /= 2
        c = (a+b)/2
    return c

def f(x):
  return math.atan(x) - 1

czasy = []
dlugosci = []

for n in range(1, 101):
    p_n = (0, 10*n)
    czas = zmierz_raz(lambda: bisekcja(f, *p_n))
    czasy.append(czas)
    dlugosci.append(10*n)

plt.plot(dlugosci, czasy)
plt.xlabel("Długość przedziału (a,b)")
plt.ylabel("Czas wykonania (s)")
plt.show()