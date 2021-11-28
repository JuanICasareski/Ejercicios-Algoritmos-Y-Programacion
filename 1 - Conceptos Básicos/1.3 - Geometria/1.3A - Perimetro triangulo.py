
def perimetroTriangulo(base, altura):
    hipotenusa = ((base/2)**2 + altura**2)*.5
    perimetro = base + 2*hipotenusa
    
    return perimetro