
def multiplosDeK(lista:list, k):
    for i, n in enumerate(lista):
        if not n%k == 0:
            del lista[i]
    return lista
