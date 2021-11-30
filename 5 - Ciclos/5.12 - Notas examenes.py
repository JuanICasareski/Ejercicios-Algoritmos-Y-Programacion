# Creo q hay q pedir solo una vez el % para aprobar

def pedirNotas():
    notas = list()

    while 1:
        nEjercicios = int(input("Ingrese la cantidad de ejercicios por examen(-1 para salir): "))
        if nEjercicios == -1:
            break
        
        pEjercicios = float(input("Ingrese el porcentaje minimo para aprobacion(como 40.3): "))
        ejerciciosResueltos = int(input("Ingrese la cantidad de ejercicios resueltos correctamente: "))
        
        pCorrecto = round(ejerciciosResueltos/nEjercicios*100, 0)
        notas.append((pCorrecto, "Aprobado" if pCorrecto >= pEjercicios else "Desaprobado"))

    for i, (porcentaje, nota) in enumerate(notas):
        print(f"{i+1}: {porcentaje}%, {nota}")
