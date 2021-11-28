
n = int(input("Ingrese el número maximo del dominó: "))

for i in range(1, n+1):
    for j in range(i, n+1):
        print(f"{i}:{j}")

