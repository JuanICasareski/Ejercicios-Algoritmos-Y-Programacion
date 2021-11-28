
def esPar(n):
    return False if n%2 else True

n1 = int(input("Ingrese el 1er número: "))
n2 = int(input("Ingrese el 2do número: "))

for n in range(min(n1, n2)+1, max(n1, n2)):
    if esPar(n):
        print(n)
