
def matrizIdentidad(dimension):
    for i in range(dimension):
        for j in range(dimension):
            print(1 if i == j else 0, end='')
        print('')
