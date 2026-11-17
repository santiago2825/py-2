while True:
    try:
        numero = float(input("ingresa un numero:"))
        break
    except ValueError:
        print("ese no es un numero")
print("el numeroes",numero)