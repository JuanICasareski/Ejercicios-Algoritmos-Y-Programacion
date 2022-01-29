
def filter(f, lista):
    resultado = []
    for i in lista:
        if f(lista):
            resultado.append(i)
    return resultado

