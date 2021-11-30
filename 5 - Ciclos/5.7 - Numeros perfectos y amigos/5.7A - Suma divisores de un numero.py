
def sumaDivisores(n):
    suma = int()
    for i in range(1, n):
        if n%i == 0:
            suma += i
    return suma
