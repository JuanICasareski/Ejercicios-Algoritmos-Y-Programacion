# Francamente no entendí como debe tomar el intervalo, asi que lo hice con horario de inicio y fin

def intervaloSegs(inicio, fin):
    '''Toma dos horas comos str, con el formato "HH:MM:SS" y devuelve la duracion del intervalo entre estas en segundos'''
    
    horaInicio, minutoInicio, segundoInicio = [int(i) for i in inicio.split(':')]
    horaFin, minutoFin, segundoFin = [int(i) for i in fin.split(':')]

    horasIntervalo = horaFin - horaInicio
    minutosIntervalo = minutoFin - minutoInicio
    segundosIntervalo = segundoFin - segundoInicio

    return (horasIntervalo*60 + minutosIntervalo)*60 + segundosIntervalo
