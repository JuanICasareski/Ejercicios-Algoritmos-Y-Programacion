
def cantidadCaracteres(string):
    dicc = {}
    for c in string:
        if c in dicc:
            dicc[c] += 1
        else:
            dicc[c] = 1
    return dicc