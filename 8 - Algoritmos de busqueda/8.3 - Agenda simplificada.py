
def agendaSimplificada(string, contactos:list):
    for i, contacto in enumerate(contactos):
        nombre = contacto[0]
        if not string in nombre:
            del contactos[i]
    return contactos
