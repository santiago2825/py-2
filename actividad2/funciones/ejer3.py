def calcular(km):
    millas = km*0.621
    return millas

kilometros = float(input("calcular a millas: "))
resultado = calcular(kilometros)
print("el resultado es:",resultado)
