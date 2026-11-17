def dividir_segura(a,b):
    if b == 0:
        print("no se puede dividir entre CERO")
        return None
    return a/b

#divisiones
print("primera division")
ejer1 = dividir_segura(10,2)
print(ejer1)
print("seguna division")
ejer2 = dividir_segura(5,0)
print(ejer2)
