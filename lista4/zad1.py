#lista = [1,1]

lista = [1,1,5,2,-1]
def inwersje(lista):
    lista_inwersji = []
    
    for k in range(0,len(lista)):
        elem = lista[k]
        for m in range(k+1,len(lista)):
            if elem > lista[m]:
                lista_inwersji.append((elem,lista[m]))
    
    return lista_inwersji

def rangi(lista):
    lista_rang = []
    posortowana = sorted(lista)
    for x in range(0,len(lista)):
        ranga = posortowana.index(lista[x])
        lista_rang.append(ranga)
        posortowana[ranga] = None
    return lista_rang


#print(rangi(lista))
#print(inwersje(lista))