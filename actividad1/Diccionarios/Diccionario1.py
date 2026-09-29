# Diccionario con los datos del producto
producto = {
    "nombre": "Maus",
    "precio": 30000,
    "cantidad_stock": 10
}
# Muestra los datos iniciales
print("Producto:", producto["nombre"])
print("Precio:", producto["precio"])
print("Stock:", producto["cantidad_stock"])

# Se realiza una venta
producto["cantidad_stock"] -= 1
# Muestra el inventario actualizado
print("Stock después de la venta:", producto["cantidad_stock"])