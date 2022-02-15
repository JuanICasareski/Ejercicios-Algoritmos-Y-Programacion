
def valorMaximoConPosicion(lista):
    max = float('-inf'), None
    for i, v in enumerate(lista):
        if v > max[0]:
            max = v, i
    return list(max)
