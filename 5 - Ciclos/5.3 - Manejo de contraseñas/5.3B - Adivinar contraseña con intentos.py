
contraseña = "Boenas"
intentos = int()

contraseñaIngresada = input("\nIngrese la contraseña: ")
while contraseña != contraseñaIngresada:
    intentos += 1
    if intentos >= 5:
        print("\n\tSe realizaron demasiados intentos.\n")
        raise SystemExit

    print("\nContraseña incorrecta, intente nuevamente.")
    contraseñaIngresada = input("Ingrese la contraseña nuevamente: ")

print("\n\tContraseña correcta.\n")
