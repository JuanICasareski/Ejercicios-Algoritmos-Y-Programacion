
def busquedaOInsertar(lista, n):  
    bajo = 0  
    alto = len(lista) - 1  
    medio = 0  

    while bajo <= alto:    
        medio = (alto + bajo) // 2  
        if lista[medio] < n:  
            bajo = medio + 1  
        elif lista[medio] > n:  
            alto = medio - 1  
        else:  
            return medio  

    lista.append(n)
    for i, v1 in enumerate(lista):
        for j, v2 in enumerate(lista):
            if v1 < v2:
                lista[i], lista[j] = lista[j], lista[i]
