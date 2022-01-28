
def esPrimo(n):
    if n == 0:
        return False
    if n == 1:
        return True 
    for i in range(2, n):
        if n%2 == 0:
            return False
    return True


def soloPrimos(lista:list):
    for i, n in enumerate(lista):
        if not esPrimo(n):
            del lista[i]
    return lista
