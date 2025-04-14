class Estudiante:
    def __init__(self, nombre, carrera, nota):
        self.nombre=nombre
        self.carrera=carrera
        self.nota=nota
    def aprobado(self):
        if self.nota>='7':
            print('El estudiante ', self.nombre,'ha aprobado la carrera de ', self.carrera,' con una nota final de ',self.nota)
        else:
            print('El estudiante ', self.nombre,'ha reprobado la carrera de ', self.carrera,'con una nota final de', self.nota)

estudiante1=Estudiante('Gabriel','Medicina','6')
estudiante2=Estudiante('Andres','Psicologia','9')

print(estudiante1.aprobado())
print(estudiante2.aprobado())