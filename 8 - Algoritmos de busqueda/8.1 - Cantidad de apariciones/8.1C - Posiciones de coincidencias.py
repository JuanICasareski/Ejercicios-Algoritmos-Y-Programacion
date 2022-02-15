
def posicionEn(lista, parametro):
    posiciones = []
    for i, v in enumerate(lista):
        if parametro == v:
            posiciones.append(i)
    return posiciones
