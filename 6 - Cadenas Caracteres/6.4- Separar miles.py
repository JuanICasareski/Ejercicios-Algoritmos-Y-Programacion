
def separarMiles(string):
    contador = int(1)
    resultado = list()

    for c in string[::-1]:
        if contador == 3:
            contador = 0
            resultado += c + "."
        else:
            resultado += c
        contador += 1
    
    if len(string)%3 == 0:
        resultado = resultado[0:-1]

    return ''.join(resultado[::-1])
