from random import randrange

def adivinarNumero():
    n = randrange(1, 10)

    nAdivinado = int(input("\nIngrese el numero que adivina: "))
    while n != nAdivinado:
        if nAdivinado < n:
            print("El número a adivinar es mayor")
        elif nAdivinado > n:
            print("El número a adivinar es menor")
        nAdivinado = int(input("Ingrese el número nuevamente: "))
    print(f"Correcto! El número era: {n}")