
def productoEscalar(v1:tuple, v2:tuple):
    V1x, V1y = v1
    V2x, V2y = v2
    return V1x*V2x + V1y*V2y


def sonOrtogonales(v1:tuple, v2:tuple):
    return productoEscalar(v1, v2) == 0
