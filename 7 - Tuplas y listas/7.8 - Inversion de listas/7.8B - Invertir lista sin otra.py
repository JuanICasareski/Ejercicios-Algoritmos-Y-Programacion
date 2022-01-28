
def invertir(lista:list):
    largo = len(lista)

    for i in range(largo):
        lista.insert(largo-i, lista[i])

    del lista[:largo]
    
    return lista
