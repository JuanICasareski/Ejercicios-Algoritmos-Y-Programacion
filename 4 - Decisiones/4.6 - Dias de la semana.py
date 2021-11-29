
def diaDeLaSemana(diasTranscurridos):
    diasSemana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
    diasTranscurridos -= (diasTranscurridos//7)*7
    return diasSemana[diasTranscurridos-1]
