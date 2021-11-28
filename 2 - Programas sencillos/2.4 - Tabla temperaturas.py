
def celsius(fahrenheit):
    '''Convierte grados Fahrenheit a Celsius'''
    return (9/5)*fahrenheit + 32

print("Fahrenheit | Celsius")

for t in range(0, 130, 10):
    print(t, celsius(t))