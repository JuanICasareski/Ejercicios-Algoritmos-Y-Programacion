
def esBisiesto(año):
    if not año%4 and (año%100 or not año%400):
        return True
    return False

def diasMes(mes, año):
    '''Toma el mes (ej: "Febrero") y el año, para devolver la cantidad de dias de ese men en ese año'''
    diasPorMes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if mes == 2 and esBisiesto(año):
        return 29
    return diasPorMes[mes]

def validarFecha(dia, mes, año):
    if dia <= diasMes(mes, año) and 0<mes<=12:
        return True
    return False

def diasMesFaltantes(dia, mes, año):
    if not validarFecha(dia, mes, año):
        raise ValueError("La fecha ingresada no es valida")
    diasRestantes = diasMes(mes, año) - dia
    return diasRestantes

def diasAñoFaltantes(dia, mes, año):
    dias = int()
    for mes in range(mes, 12):
        dias += diasMes(mes, año)
    dias += diasMesFaltantes(dia, mes, año)
    return dias


def diasTranscurridosAño(dia, mes, año):
    if esBisiesto(año):
        return 366-diasAñoFaltantes(dia, mes, año)
    return 365-diasAñoFaltantes(dia, mes, año)
