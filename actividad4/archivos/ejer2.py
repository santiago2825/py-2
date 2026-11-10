ventas=[45000, 120000,8000, 300000]

with open('ventas.txt', 'w', encoding="utf-8") as f:
    for valor in ventas:
        f.writelines(str(valor) + '\n')
with open('ventas.txt', 'r', encoding="utf-8") as f:
    suma = 0
    for valor in f:
        suma += int(valor)
    print("La suma de las ventas es:", suma)
