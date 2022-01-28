
def fichasDominoEncajan(ficha1:str, ficha2:str):
    for n1 in ficha1.split('-'):
        for n2 in ficha2.split('-'):
            if n1 == n2:
                return True
    return False
