
def NWW(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def dzialki(n):

    wszystkie_podzialy = []

    for dzieci in range(1,n+1):
        for podziały in range(1,dzieci):
            podział = f"{podziały}/{dzieci}"
            for x in range(2,dzieci+1):
                if NWW(podziały, dzieci) != 1:
                    break
                if podział not in wszystkie_podzialy:
                    wszystkie_podzialy.append(podział)
        
    return len(wszystkie_podzialy) + 1

print(dzialki(100))