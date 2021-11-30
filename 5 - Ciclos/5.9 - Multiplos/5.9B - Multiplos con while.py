
def multiplosEntreAlt(n1,n2):
    '''Donde n1 es el divisor y n2 es el numero maximo'''
    i = n1
    numeros = []
    while i < n2:
        numeros.append(i)
        i += n1
    return numeros
