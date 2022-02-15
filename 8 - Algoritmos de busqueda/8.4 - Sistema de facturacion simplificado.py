
def facturacionSimplificada(precios, productos):
    total = 0
    print("id | nombre | precio | cantidad | total")
    for id, q in productos: 
        for producto in precios:
            if id == producto[0]:
                datos = producto

        totalProducto = producto[2]*q
        total += totalProducto
        print(f"{producto[0]} | {producto[1]} | {producto[2]} | {q} | {totalProducto}")
    
    print(f"                          Total: {total}")
