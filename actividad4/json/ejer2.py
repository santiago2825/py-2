import json 

class Carrito:
    def __init__(self):
        self.productos = []
    def agregar(self,producto,precio,stock):
        self.productos.append({
            "producto":producto,
            "precio":precio,
            "stock":stock
        })
    def guardar(self, archivo):
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.productos, f, indent=4, ensure_ascii=False)
        print("archivo guardado")
    def cargar(self, archivo):
        with open(archivo, "r", encoding="utf-8")as f:
            self.productos = json.load(f)
        print("archivo cargado")
    def mostrar(self):
        for item in self.productos:
            print(item)

#creamos los carritos
#creamos el primer carrito
Carrito1 = Carrito()
#creamos los productos al carrito
Carrito1.agregar("camisa",50000,23)
Carrito1.agregar("pantalon",75000,12)
print("contenido del carrito 1")
Carrito1.mostrar()
#guardamos
Carrito1.guardar("carrito.json")
#creamos el segundo carrito
Carrito2 = Carrito()
#hacemos una condicional para verificar que el segundo carrito no tenga productos
if not Carrito2.productos:
    print("el carrito 2 esta vacio")
#le cargamos los datos del primer carrito al segundo carrito
Carrito2.cargar("carrito.json")
#y mostramos los productos
Carrito2.mostrar()
