
def esPrimo(n):
    for i in range(2, n):
        if n%i == 0:
            return True
    return False
