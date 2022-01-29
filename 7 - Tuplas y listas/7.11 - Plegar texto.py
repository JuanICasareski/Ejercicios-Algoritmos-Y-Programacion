
def plegarTexto(string, largo):
    resultado = []
    for palabra in string.split(' '):
        palabra = list(palabra)
        while 1:
            if palabra[:largo] == []:
                break
            resultado.append(''.join(palabra[:largo]))
            del palabra[:largo]
    
    return resultado

#   Nota: No estoy completamente seguro a que se refiere con "Respetar los espacios".
# Por lo tanto hice que agrupe las letras de las palabras sin contar las de otras palabras
