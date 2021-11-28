
def unidadEntero(n):
    # Transforma el n en un str (para que sea subscriptable), seleccióna su ultimo numero y lo convierte nuevamente a un entero
    return int(str(n)[-1])
