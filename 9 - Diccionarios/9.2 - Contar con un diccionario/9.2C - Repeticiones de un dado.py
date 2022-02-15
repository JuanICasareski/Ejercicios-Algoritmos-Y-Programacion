from random import randint

def cantidadNumeros(rep):
    dicc = {}
    numeros = [randint(1,6) for _ in range(rep)]
    for n in numeros:
        if n in dicc:
            dicc[n] += 1
        else:
            dicc[n] = 1
    return dicc
