class Cliente:
    def __init__(self, nombre, membresia_activa):
        self.nombre = nombre
        self.membresia_activa = membresia_activa

    def entrar(self):
        if self.membresia_activa:
            return f"{self.nombre} puede entrar"
        else:
            return f"{self.nombre} no puede entrar (membresia inactiva)"

cliente = Cliente("santiago", False)
cliente2 = Cliente("nicolas", False)

print(cliente.entrar())
print(cliente2.entrar())