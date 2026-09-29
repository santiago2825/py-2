def propina(cuenta, porcentaje=10):
    propina = cuenta * (porcentaje / 100)
    total = cuenta + propina    
    return propina, total
print(propina(5000))