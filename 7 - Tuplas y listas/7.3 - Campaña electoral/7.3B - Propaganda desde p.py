
def propagandaDesdeN(nombre:tuple, n:int, p:int):
    for i, nombre in enumerate(nombre):
        if  p <= i+1 <= p+n:
            print(f"Estimado {nombre}, vote por mi.")
