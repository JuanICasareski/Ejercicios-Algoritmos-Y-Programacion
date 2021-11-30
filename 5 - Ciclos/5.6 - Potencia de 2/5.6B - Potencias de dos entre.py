
def esPotenciaDos(n):
    while 1:
        if not n%2:
            n /= 2
        else:
            return False
        if n==2 or n==1:
            return True


def potenciasDosEntre(n1,n2):
    numerosEntre = list()
    for i in range(n1,n2):
        if esPotenciaDos(i):
            numerosEntre.append(i)
    return numerosEntre
