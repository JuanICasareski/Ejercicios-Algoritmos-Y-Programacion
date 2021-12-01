
def pedirNumero(mensaje, min, max):
    while 1:
        msg = input(mensaje)
        try:
            msg = int(msg)
            if min <= msg <= max:
                return msg
            print(f"El dato debe estar entre {min} y {max}")
        
        except ValueError:
            print("El dato ingresado no es un número")

# Francamento no es mi meojr implementación de un ejercicio