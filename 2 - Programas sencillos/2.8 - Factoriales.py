
def factorial(n):
    resultado = n
    for i in range(1, n):
        resultado *= i  
    return resultado
    
numeros = list()    
while 1:
    n = int(input("Ingrese un numero a calcular le factorial (-1 para salir): "))
    if n == -1:
        break
    numeros.append(factorial(n))

for i, n in enumerate(numeros):
    print(f"{i} - {n}")