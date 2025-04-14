class Pajaro:
    def sonido(self):
        print("El pajaro hace pio")

class Gato:
    def sonido(self):
        print("El gato hace Miau")

def hacer_sonido(animal):
    animal.sonido()
    
gato=Gato()
pajaro=Pajaro()

hacer_sonido(gato)
hacer_sonido(pajaro)