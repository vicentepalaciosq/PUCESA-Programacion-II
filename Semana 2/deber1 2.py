class Estudiante:
    def __init__(self,nombre,carrera,nfinal):
        self.nombre=nombre
        self.carrera=carrera
        self.nfinal=nfinal
    
    def aprobar(self):
        if self.nfinal >="7":
            print(f"El estudiante {self.nombre} ha aprobado la carrera de {self.carrera} con un promedio de {self.nfinal}")
        else:
            print(f"El estudiante {self.nombre} ha reprobado la carrera de {self.carrera} con un proomedio de {self.nfinal}")


estudiante1=Estudiante('Vicente', 'Ingenieria en sistemas','8')
estudiante2=Estudiante('Gabriel','Medicina','5')

estudiante1.aprobar()
estudiante2.aprobar()