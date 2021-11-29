
def signoSodiacal(dia:int, mes:int) -> str:
    '''Toma el dia y mes de nacimiento para devolver su signo sodiacal'''
    if (dia>=21 and mes==3) or (dia<=20 and mes==4):
        return "Aries"
    if (dia>=24 and mes==9) or (dia<=23 and mes==10):
        return "Libra"
    if (dia>=21 and mes==4) or (dia<=21 and mes==5):
        return "Tauro"
    if (dia>=24 and mes==10) or (dia<=22 and mes==11):
        return "Escorpio"
    if (dia>=22 and mes==5) or (dia<=21 and mes==6):
        return "Géminis"
    if (dia>=23 and mes==11) or (dia<=21 and mes==12):
        return "Sagitario"
    if (dia>=21 and mes==6) or (dia<=23 and mes==7):
        return "Cáncer"
    if (dia>=22 and mes==12) or (dia<=20 and mes==1):
        return "Capricornio"
    if (dia>=24 and mes==7) or (dia<=23 and mes==8):
        return "Leo"
    if (dia>=21 and mes==1) or (dia<=19 and mes==2):
        return "Acuario"
    if (dia>=24 and mes==8) or (dia<=23 and mes==9):
        return "Virgo"
    if (dia>=20 and mes==2) or (dia<=20 and mes==3):
        return "Piscis"    
    raise ValueError("La fecha ingresada es invalida")

dia = input("Ingrese su mes de nacimiento: ")
mes = input("Ingrese su mes de nacimiento: ")
print(f"Su signo sodiacal es: {signoSodiacal(dia, mes)}")

