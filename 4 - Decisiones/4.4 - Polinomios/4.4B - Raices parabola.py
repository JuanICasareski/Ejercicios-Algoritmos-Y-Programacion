
def raicesParabola(a, b, c):
    if a == 0:
        raise ValueError("Se debe ingresar una parabola con primer coeficiente distinto a 0")
    r1 = (-b + (b**2 -4*a*c)**.5) / (2*a)
    r2 = (-b - (b**2 -4*a*c)**.5) / (2*a)

    return r1, r2
    