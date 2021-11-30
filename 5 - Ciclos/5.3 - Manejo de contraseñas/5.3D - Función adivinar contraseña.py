from time import sleep

def adivinarContraseña() -> bool:
    contraseña = "Boenas"
    intentos = int()

    contraseñaIngresada = input("\nIngrese la contraseña: ")
    while contraseña != contraseñaIngresada:
        intentos += 1
        if intentos >= 5:
            return False

        sleep(1.5*intentos)
        
        print("\nContraseña incorrecta, intente nuevamente.")
        contraseñaIngresada = input("Ingrese la contraseña nuevamente: ")

    return True
