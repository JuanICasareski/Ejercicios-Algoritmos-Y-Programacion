def esPrimo(n):
    for i in range(2, 9):
        if not n%i and n != i:
            return False
    return True


def primosHasta(limite):
    primos = list()
    for n in range(limite+1):
        if esPrimo(n):
            primos.append(n)
    return primos
