def xgcd(a, b):
    if b==0:
        return (a, 1, 0)
    else:
        (gcd, x_prim, y_prim) = xgcd(b, a%b)
        return (gcd, y_prim, x_prim-a//b*y_prim)
#podpunkt 1
def diofantyczne_ma_rozwiązanie(a, b, c):
    gcd, x, y = xgcd(a,b)
    if c % gcd == 0:
        return True
    else:
        return False
    
#print(diofantyczne_ma_rozwiązanie(18, 16, 500) is True)

#podpunkt 2
def diofantyczne_rozwiązanie(a,b,c):
    if diofantyczne_ma_rozwiązanie(a,b,c):
        gcd, x, y = xgcd(a,b)
        ile = c/gcd
        return(x*ile,y*ile)
    else:
        return None

print(diofantyczne_rozwiązanie(4, 8, 12))
#podpunkt 3
def diofantyczne_nieujemne(a,b,c):
    if diofantyczne_ma_rozwiązanie(a,b,c):
        maxx = c//a + 1
        maxy = c//b + 1
        rozwiazania = []
        for dlax in range(1,maxx):
            for dlay in range(1,maxy):
                if a*dlax + b*dlay == c:
                    rozwiazania.append((dlax,dlay))
        if rozwiazania:
            return rozwiazania
        return None
#print(diofantyczne_nieujemne(18, 16, 500))

def diofantyczne_zad(a,b,c):
    if diofantyczne_ma_rozwiązanie(a,b,c):
        gcd = xgcd(a,b)[0]
        x,y = diofantyczne_rozwiązanie(a,b,c)
        sumak = abs(x) + abs(y)
        ''' ogolne wzory
        xk = x + b/gcd * k
        yk = y - a/gcd * k
        '''
        xkk = x
        ykk = y

        for k in range(0,1000):
            xk = x + b/gcd * k
            yk = y - a/gcd * k
            suma = abs(xk) + abs(yk)
            if suma < sumak:
                sumak = suma
                xkk = xk
                ykk = yk
        return sumak, xkk, ykk
    
def diof_poprawka(a,b,c):
    if diofantyczne_zad(a,b,c):
        suma1, xkk1, ykk1 = diofantyczne_zad(a,b,c)
        suma2, xkk2, ykk2 = diofantyczne_zad(b,a,c)
        if suma1 < suma2:
            return xkk1, ykk1
        else:
            return xkk2, ykk2
    


#zadania
'''dskok = 228
kskok = 84
dom = 430
horacy = 432'''
kskok = 84
dskok = 228
dom = 11
horacy = 432
print(f'Horacy: {int(diof_poprawka(kskok,dskok,horacy)[0])} krótkie, {int(diof_poprawka(kskok,dskok,horacy)[1])} długie')
print(f'Dom: {diof_poprawka(kskok,dskok,dom)}')
