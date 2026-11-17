try:
    with open("datos.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("el archivo no existe")