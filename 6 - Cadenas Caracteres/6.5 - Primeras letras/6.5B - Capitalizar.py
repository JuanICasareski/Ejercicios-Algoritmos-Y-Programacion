
def capitalizar(string):
    palabras = string.split(' ')
    resultado = list()
    
    for palabra in palabras:
        resultado.append(palabra.capitalize())
    return ' '.join(resultado)
