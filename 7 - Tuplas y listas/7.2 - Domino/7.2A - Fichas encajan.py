
def fichasDominoEncajan(ficha1:tuple, ficha2:tuple):
    for n1 in ficha1:
        for n2 in ficha2:
            if n1 == n2:
                return True
    return False