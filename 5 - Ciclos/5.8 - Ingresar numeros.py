numeros = list()

while 1:
    numero = int(input("\n\t Ingrese un número (-1 para salir): "))
    if numero  == -1:
        break
    numeros.append(numero)

print('\n\t Numeros ingresados: ', len(numeros))
print('\t Suma total de los valores: ', sum(numeros))
print('\t El promedio de los numeros ingresados es de: ', sum(numeros)/len(numeros))