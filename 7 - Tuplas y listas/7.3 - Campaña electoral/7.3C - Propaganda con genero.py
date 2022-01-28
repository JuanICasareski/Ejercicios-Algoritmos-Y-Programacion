
def propagandaNombrePorGenero(nombres:tuple):
    for nombre, genero in nombres:  
        print(f"Estimado {nombre}, vote por mi." if genero == "masculino" else f"Estimada {nombre}, vote por mi.")