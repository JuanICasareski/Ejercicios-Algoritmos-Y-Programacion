
def verticeParabola(a, b, c):
    puntoInflexionX = -b/(2*a)
    puntoInflexionY = a*puntoInflexionX**2 + b*puntoInflexionX + c
    return ('max', (puntoInflexionX, puntoInflexionY)) if a<0 else ('min', (puntoInflexionX, puntoInflexionY))
