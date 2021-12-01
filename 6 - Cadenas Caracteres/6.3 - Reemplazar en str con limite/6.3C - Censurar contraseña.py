
def censurarContraseña(string, n):
    resultado = list()
    contador = int(1)
    
    for c in string:
        if contador > n:
            resultado += c
        else: 
            resultado += "X"
            contador += 1
    return resultado
