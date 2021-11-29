
def romano(n:int) -> str:
    '''Toma un año en arábigo y lo devuelve en romano'''
    
    # Separa milenas, centenas, decenas y unidades
    milena = int(n/1000)
    centena = int((n -(milena*1000))/100)
    decena = int((n -(milena*1000 + centena*100))/10)
    unidad = (n -(milena*1000 + centena*100 + decena*10))

    numeroRomano = str()

    # Itera entre milena, centena, etc. con sus correspondientes simbolos
    for i, j in zip((milena, centena, decena, unidad), (("M","V|","X|"), ("C","D","M"), ("X","L","C"), ("I", "V", "X"))):
        u = j[0]  # Defino el simbolo para la unidad
        q = j[1]  # Defino el simbolo para las 5 unidades
        d = j[2]  # Defino el simbolo para la decena

        if i <= 3:
            numeroRomano += f"{u}"*i 
        if i == 4:
            numeroRomano += f"{u}{q}"
        if 5 <= i <= 8:
            numeroRomano += f"{q}" + f"{u}"*(i-5)
        if i==9:
            numeroRomano += f"{u}{d}"
        
    return numeroRomano

año = int(input("Ingrese el año a convertir a romano: "))
print(f"\nEl año {año} en romano seria: {romano(año)}")
