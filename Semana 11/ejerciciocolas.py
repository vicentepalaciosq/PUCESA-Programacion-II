class ColaPrioridadHospital:
    def __init__(self):
        self.items=[]
    def encolar(self,paciente,prioridad):
        self.items.append((prioridad,paciente))
        return paciente, prioridad
    def vacia(self):
        return len(self.items) == 0
    def desencolar(self):
        if not self.vacia():
            self.items.sort(key=lambda x: x[0])
            atendido=self.items.pop(0)
            print('Paciente:',atendido[1],'atendido')
        else:
            print('No hay pacientes por atender')
    def tamano(self):
        print('Hay',len(self.items),'personas en cola')
    def mostrar_pendientes(self):
        for prioridad,pacientes in sorted(self.items, key=lambda x: x[0]):
            print('Paciente:',pacientes,'prioridad:', prioridad)


cola_pacientes=ColaPrioridadHospital()


cola_pacientes.encolar('Vicente',1)
cola_pacientes.encolar('Adrian',4)
cola_pacientes.encolar('Sebastian',5)
cola_pacientes.encolar('Gabriela',3)
cola_pacientes.encolar('Esteban',3)
cola_pacientes.encolar('Carla',2)
cola_pacientes.encolar('Alison',4)
cola_pacientes.encolar('Alejandro',1)


while True:
    print('Menu de Opciones')
    print('1. Mostrar pendientes en cola')
    print('2. Desencolar')
    print('3. Mostrar tamano')
    print('4. Agregar paciente')
    print('5. Salir')
    opcion=int(input('Ingrese una opcion: '))
    if opcion==1:
        cola_pacientes.mostrar_pendientes()
    elif opcion==2:
        cola_pacientes.desencolar()
    elif opcion==3:
        cola_pacientes.tamano()
    elif opcion==4:
        paciente=input('Ingrese el nombre del paciente: ')
        prioridad=int(input('Ingrese la prioridad del paciente: '))
        cola_pacientes.encolar(paciente,prioridad)
        print('Paciente:',paciente,'agregado con prioridad:',prioridad)
    elif opcion==5:
        print('Gracias por usar el programa!')
        break
    else:
        print('Ingrese una opcion valida')