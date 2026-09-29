class Vehiculos:
    def __init__(self, placa, conductor, disponible = False):
        self.placa = placa
        self.conductor = conductor
        self.disponible = disponible
    def estado(self):
        if self.disponible:
            self.disponible=False
            print(f"el vehiculo {self.placa} ({self.conductor}) ahora esta ocupado")
        else:
            self.disponible = True
            print(f"el vehiculo {self.placa} ({self.conductor}) ahora esta disponible")

auto = Vehiculos("wew-we2","santiago")
auto.estado()