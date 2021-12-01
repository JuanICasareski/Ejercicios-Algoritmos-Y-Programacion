
def sigla(string):
    palabras = string.split(' ')
    resultado = list()
    for palabra in palabras:
        resultado.append(palabra[0].upper())
    return ''.join(resultado)
