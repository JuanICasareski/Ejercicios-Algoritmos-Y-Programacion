
# Rta: 
# (Suponiendo que la dificultad para ejecutar una división (o una multiplicación)
# es la misma que la de ejecutar una suma)
# Iterar entre n y 1 usa mas calculos para números menores a 4

n = int(input("Ingrese la cantidad de números triangulares a mostrar: "))
triangular = int()

for i in range(1, n+1):
    triangular += i
    print(f"{i} - {triangular}")