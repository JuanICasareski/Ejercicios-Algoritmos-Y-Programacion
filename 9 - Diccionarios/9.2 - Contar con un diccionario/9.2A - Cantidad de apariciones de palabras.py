
def cantidadPalabras(texto):
    dicc = {}
    for palabra in texto.split(' '):
        if palabra in dicc:
            dicc[palabra] += 1
        else:
            dicc[palabra] = 1
    return dicc
