
def separarIP(string, n):
    cambios = int()
    contador = int(1)
    resultado = list()

    for c in string:
        if contador == 3 and cambios <= n:
            contador = 0
            cambios += 1
            resultado += c + "."
        else:
            resultado += c
        contador += 1
    
    return ''.join(resultado)
