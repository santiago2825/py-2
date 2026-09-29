edades = [15, 22, 17, 30, 16, 25]
# Listas vacías para guardar los resultados
mayores = []
menores = []
# Clasifica cada edad
for edad in edades:
    if edad >= 18:
        mayores.append(edad)
    else:
        menores.append(edad)
# Muestra los dos grupos
print("Mayores de edad",mayores)
print("Menores de edad",menores)
