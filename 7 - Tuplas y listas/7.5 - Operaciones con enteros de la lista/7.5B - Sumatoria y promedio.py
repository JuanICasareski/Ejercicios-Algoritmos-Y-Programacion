
def sumatoriaYPromedio(lista:list):
    suma = int()
    for n in lista:
        suma += n
    return suma, suma/len(lista)
