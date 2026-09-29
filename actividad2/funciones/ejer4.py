def calcular_descuento(lista):
    con_descuento = []
    sin_desceunto = []
    for precio in lista:
        if precio>100000:
            precio_final = precio * 0.85
            con_descuento.append(precio_final)
        else:
            sin_desceunto.append(precio)
    return con_descuento, sin_desceunto

precios = [1000, 3000, 450000, 230000, 6700]
con_desc, sin_desc= calcular_descuento(precios)
print("precios con descuento",con_desc)
print("precios sin descuento",sin_desc)