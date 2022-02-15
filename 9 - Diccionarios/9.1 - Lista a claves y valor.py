
def listaAClaves(lista):
    dicc = {}
    for clave, valor in lista:
        if clave in dicc:
            dicc[clave].append(valor)
        else:
            dicc[clave] = [valor]
    return dicc
