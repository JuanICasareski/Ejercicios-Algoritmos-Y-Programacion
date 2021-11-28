
def normaVectorial(x, y, z):
    return (x**2 + y**2 + z**2)**.5

def productoVectorial(x1, y1, z1, x2, y2, z2):
    return y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2

def diferenciaVectorial(x1, y1, z1, x2, y2, z2):
    return x1-x2, y1-y2, z1-z2


def areaTrianguloEntrePuntos(Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz):
    ABx, ABy, ABz = diferenciaVectorial(Ax, Ay, Az, Bx, By, Bz)
    ACx, ACy, ACz = diferenciaVectorial(Ax, Ay, Az, Cx, Cy, Cz)

    Px, Py, Pz = productoVectorial(ABx, ABy, ABz, ACx, ACy, ACz)
    return normaVectorial(Px, Py, Pz)/2
