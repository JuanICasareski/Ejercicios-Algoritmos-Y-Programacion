
def separarIP(string):
    contador = int(1)
    resultado = list()

    for c in string:
        if contador == 3:
            contador = 0
            resultado += c + "."
        else:
            resultado += c
        contador += 1
    
    return ''.join(resultado)
