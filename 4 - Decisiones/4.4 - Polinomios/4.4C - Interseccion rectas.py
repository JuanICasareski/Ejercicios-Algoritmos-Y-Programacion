
def interseccionRectas(pendiente1, ordenada1, pendiente2, ordenada2):
    if pendiente1 == pendiente2:
        raise ValueError("Las rectas no pueden ser paralelas")
    interseccionX = (ordenada1-ordenada2)/(pendiente1-pendiente2)
    interseccionY = ordenada1*interseccionX+ordenada1
    
    return interseccionX, interseccionY
