import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}
df = pd.DataFrame(inventario)
df.to_csv('inventario.csv', index=False)
print("archivo guardado")
df_leido =pd.read_csv('inventario.csv')
print("\n datos originales:")
print(df)
print("\n datos leidos desde el archivo:")
print(df_leido)
if df.equals(df_leido):
    print("\n los datos son iguales")
else:
    print("\n los datos no son iguales ")
