productos = [
    {"nombre":"camisa", "precio":222222},
    {"nombre":"pantalon", "precio":50000},
    {"nombre":"zapato", "precio":24000},
    {"nombre":"cahaqueta", "precio":250000},
]
oferta =[p["nombre"]for p in productos if p["precio"]<50000]
print("producto en ofertas:", oferta)