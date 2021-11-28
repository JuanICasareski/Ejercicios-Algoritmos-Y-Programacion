# Francamente no entendí como debe tomar el intervalo, asi que lo hice con horario de inicio y fin

def intervaloHoras(segundoInicio, segundoFin):
    '''Toma dos horas como segundos y devuelve el intervalo entre estas en formato "HH:MM:SS"'''

    segundosIntervalo = segundoFin - segundoInicio

    horas = segundosIntervalo//3600
    minutos = (segundosIntervalo-horas*3600)//60 
    segundos = segundosIntervalo-minutos*60

    return f"{horas}:{minutos}:{segundos}"
