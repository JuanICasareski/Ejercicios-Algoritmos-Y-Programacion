
def soloPalabrasConA(string):
    resultado = list()
    palabras = string.split(' ')
    
    for palabra in palabras:
        if palabra[0].lower() == 'a':
            resultado.append(palabra)

    return ' '.join(resultado)
