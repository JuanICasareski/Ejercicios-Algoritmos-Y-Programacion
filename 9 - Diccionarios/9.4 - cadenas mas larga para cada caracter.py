
def cadenaMasLargaPorCaracter(texto):
    dicc = {}
    for c in texto:
        if c not in dicc and c != ' ':
            dicc[c] = ''
    
    for palabra in texto.split(' '):
        for c in dicc:
            if c in palabra and len(dicc[c]) < len(palabra):
                dicc[c] = palabra
        
    return dicc
    
