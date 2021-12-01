
def binarioADecimal(nBinario:str):
    suma = int()
    for i, d in enumerate(list(nBinario[::-1])):
        suma += int(d)*(2**i)
    return suma
