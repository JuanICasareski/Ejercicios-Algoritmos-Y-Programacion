
notas = list()
while 1:
    nota = int(input("Ingrese una nota(-1 para salir): "))
    if nota == -1:
        break
    notas.append(nota)

promedio = sum(notas)/len(notas)
print(f"\nEl promedio es de: {round(promedio ,2)}")