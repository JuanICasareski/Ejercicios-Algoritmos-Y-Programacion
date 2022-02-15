
def valorMaximo(lista):
    max = float('-inf')
    for i in lista:
        if i > max:
            max = i
    return max
