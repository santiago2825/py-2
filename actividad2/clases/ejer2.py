class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio":precio})
        print(f"producto '{nombre}' valor de ${precio}")

    def total(self):
        total_pagar = sum(producto["precio"] for producto in self.productos)
        return total_pagar

mi_compra = CarritoCompras()

mi_compra.agregar("camisa", 230000)
mi_compra.agregar("zapatos", 200000)

print(f"total a pagar es de: ${mi_compra.total()}")
