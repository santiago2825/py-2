import json
inventario =[
    {"producto":"camisa","precio":45000,"stock":20},
    {"producto":"gorra","precio":30000,"stock":5},
    {"producto":"pantalon","precio":89000,"stock":12},
    {"producto":"medias","precio":8000,"stock":40},
    {"producto":"zapatos","precio":150000,"stock":3},
]
with open ("inventario.json", "w", encoding="utf-8")as f:
    json.dump(inventario, f, indent=4, ensure_ascii=False)

with open ("inventario.json", "r", encoding="utf-8")as f:
    datos = json.load(f)

print("productos con stock menor a 10")
for item in datos:
    if item["stock"]<10:
        print(item)

nuevo_producto = {"producto":"bufanda","precio":25000,"stock":15}

datos.append(nuevo_producto)

with open ("inventario.json", "w", encoding="utf-8")as f:
    json.dump(datos, f, indent=4, ensure_ascii=False)
