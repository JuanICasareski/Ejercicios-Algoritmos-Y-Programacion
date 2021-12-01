
def reemplazarSiguienteVocal(string):
    vocales = ('a', 'e', 'i', 'o', 'u', 'a', 'A', 'E', 'I', 'O', 'U', 'A')
    string = list(str(string))

    for i, l in enumerate(string):
        if l in vocales:
            string[i] = vocales[vocales.index(l) + 1]

    return ''.join(string)
