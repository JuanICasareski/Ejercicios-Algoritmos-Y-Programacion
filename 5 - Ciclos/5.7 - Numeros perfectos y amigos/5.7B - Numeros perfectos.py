
def sumaDivisores(n):
    suma = int()
    for i in range(1, n):
        if n%i == 0:
            suma += i
    return suma


def primerosNumerosPerfectos(n):
    '''Nota: No usar un N mayor a 5'''
    i = 0
    contador = 0
    while 1:
        if i == sumaDivisores(i):
            print(i, sumaDivisores(i))
            contador += 1
            if contador == n:
                break
        i += 1
