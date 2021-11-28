
def montoConInteres(dinero, tasaInteres, años):
    return dinero * (1 + tasaInteres/100)**años

dinero = input("Ingrese el monto iniicial: ")
tasaInteres = input("Ingrese la tasa de interes: ")
años = input("Ingrese los años a evaluar: ")

montoFinal = montoConInteres(dinero, tasaInteres, años)
print(f"El monto final seria de: {montoFinal}")