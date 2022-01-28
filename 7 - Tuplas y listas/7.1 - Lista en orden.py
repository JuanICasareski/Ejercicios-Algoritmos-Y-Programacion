
def enOrden(tupla:tuple):
    for i, n in enumerate(tupla):
        if i == len(tupla)-1:
            break
        if not tupla[i] <= tupla[i+1]:
            return False
    return True 
