
def referenciaAK(lista:list, k):
    menores:list = list()
    mayores:list = list()
    iguales:list = list()

    for n in lista:
        if n < k:
            menores.append(n)
        elif n > k:
            mayores.append(n)
        else:
            iguales.append(n)
            
    return menores, mayores, iguales