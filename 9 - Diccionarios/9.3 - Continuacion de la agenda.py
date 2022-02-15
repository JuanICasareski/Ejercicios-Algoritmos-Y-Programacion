contactos = {}

while 1:
    nombre = input("\n\t Ingrese el nombre a buscar: ")
    if nombre in contactos:
        print(f"\t El número del contacto ingresado es: {contactos[nombre]}")
    else:
        print("\n\t El contacto indicado no existe;")
        numero = input(f"\t Ingrese el numero a asociar con {nombre}: ")
        if numero == '*':
            break
        contactos[nombre] = numero
