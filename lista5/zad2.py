def levenshtein(napis1, napis2):
    if len(napis2) == 0:
        return len(napis1)
    if len(napis1) == 0:
        return len(napis2)
    if napis1[-1] == napis2[-1]:
        return levenshtein(napis1[:-1],napis2[:-1])
    else:
        return min(levenshtein(napis1,napis2[:-1])+1,levenshtein(napis1[:-1],napis2)+1,levenshtein(napis1[:-1],napis2[:-1])+2)
    
#print(levenshtein("Ala", "Olek"))

def guess(napis, lista):
    odleglosci = {}
    minimalne = []
    for x in lista:
        odleglosci[x] = levenshtein(napis,x)
    mini = min(odleglosci.values())
    for x in lista:
        if odleglosci[x] == mini:
            minimalne.append(x)
    return minimalne

lista = ['aa','cla','bla','alc']
print(guess("ala",lista))
