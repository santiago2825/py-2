# Lista con los precios
precios = [15000, 8000, 22000, 5000]
# Variable para guardar la suma de los precios
total =0
for precio in precios:
    total += precio
    # Calcula el promedio dividiendo el total entre la cantidad de elementos
promedio= total / len(precios)
# Muestra los resultados finales
print("El total es de", total)
print("El promedio es de", promedio)