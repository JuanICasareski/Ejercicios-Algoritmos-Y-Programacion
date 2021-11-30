
def multiplosEntre(n1,n2):
    '''Donde n1 es el divisor y n2 es el numero maximo'''
    numeros = []
    for i in range(n1, n2, n1):
        if i < n2:
            numeros.append(i)
    return numeros
