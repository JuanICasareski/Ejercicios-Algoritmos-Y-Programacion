
def factorial(n):
    resultado = n
    for i in range(1, n):
        resultado *= i  
    return resultado


def listaFactoriales(lista:list):
    for i, n in enumerate(lista):
        lista[i] = factorial(n)
    return lista
