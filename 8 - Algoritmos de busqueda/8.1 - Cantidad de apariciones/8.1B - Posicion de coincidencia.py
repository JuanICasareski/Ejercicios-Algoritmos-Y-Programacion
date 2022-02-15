
def posicionEn(lista, parametro):
    for i, v in enumerate(lista):
        if parametro == v:
            return i
    return None
