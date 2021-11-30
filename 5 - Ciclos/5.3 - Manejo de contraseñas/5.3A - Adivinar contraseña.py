
contraseña = "Boenas"

contraseñaIngresada = input("\nIngrese la contraseña: ")
while contraseña != contraseñaIngresada:
    print("\nContraseña incorrecta, intente nuevamente.")
    contraseñaIngresada = input("Ingrese la contraseña nuevamente: ")

print("\n\tContraseña correcta.\n")
