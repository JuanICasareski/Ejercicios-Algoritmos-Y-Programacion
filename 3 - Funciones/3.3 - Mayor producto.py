
def mayorMultiplo(numeros:list):
    max = 2.2e-308
    for i, n1 in enumerate(numeros):
        for j, n2 in enumerate(numeros):
            if not i==j:
                if n1*n2 > max:
                    max = n1*n2
    return max
