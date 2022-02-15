
def coincidenciasEn(lista, parametro):
    n = 0
    for i in lista:
        if parametro == i:
            n += 1
    return n
