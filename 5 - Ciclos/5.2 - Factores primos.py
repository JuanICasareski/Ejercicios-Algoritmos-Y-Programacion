
def esPrimo(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


def factoresPrimos(n:int) -> None:
    '''Imprime los factores primos para el número ingresado'''
    print(f"Factores primos para {n}: ")
    factores = list()
    while n!=1:
        for i in range(2, int(n+1)):
            if n%i == 0 and esPrimo(i):
                factores.append(str(i))
                n /= i
    print("*".join(factores))