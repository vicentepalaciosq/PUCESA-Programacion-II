class Vehiculo:
    def moverse(self):
        print("El vehiculo se mueve")

class Auto(Vehiculo):
    def moverse(self):
        print("El auto puede moverse ")
        

auto=Auto()
auto.moverse()