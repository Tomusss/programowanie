def dzialki(n):
    if n == 1:
        return 1

    podzialy_wczesniejsze = dzialki(n-1)
    podzialy_dla_n = 0
    for x in range(1,n):
        check = 0
        for y in range(2,x+1):
            if x%y == 0 and n%y == 0:
                check = 1
                break
        if check == 0:
            podzialy_dla_n += 1
            #print(x,n)
        
    podzialy = podzialy_wczesniejsze + podzialy_dla_n
    return podzialy

n = int(input('Podaj liczbę dzieci: '))
print(f'Jeśli król ma {n} dzieci, to potrzebne jest {dzialki(n)} działek')
