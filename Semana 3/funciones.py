''''
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre= nombre
        self.edad= edad
        self.ocupacion=  ocupacion
    def descripcion(self):
        return f"Nombre {self.nombre}, Edad {self.edad} años, Ocupacion {self.ocupacion}"


while True:
        print('Seleccione una opcion: ')
        print('1. Agregar persona')
        print('2. Salir')
        opcion = input('Ingrese la opcion: ')
        if opcion == '1':
            personas=(Persona(input("Ingrese el nombre: "), int(input("Ingrese la edad: ")), input("Ingrese la ocupacion: ")))
            print(personas.descripcion())
        
        elif opcion==2:
            print('Adios')
            break
    '''

class Animal:
    def hablar(self):
        print('Este animal hace un sonido')

    def sonido(self):
        print('Este animal hace un sonido')

class Perro(Animal):
    def sonido(self):
        print('El perro dice GUAU!')

class Persona(Animal):
    def hablar(self):
        print('La persona puede hablar distintos idiomas')

perro=Perro()
perro.sonido()

humano=Persona()
humano.hablar()


