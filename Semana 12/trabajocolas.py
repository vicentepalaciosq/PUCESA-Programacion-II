#Hecho por: Vicente Palacios
#Fecha: 16/06/25
#Parte 2

# Reflexion final
# Explica en tus propias palabras: ¿Qué diferencias observas entre el funcionamiento de una PILA y una COLA CON PRIORIDAD?

# Pilas y colas al principio parecen lo mismo, ademas de servir para mantener un orden, usan distintos principios
# Pilas por un lado usa LIFO que significa que el ultimo que llega es el primero que sale
# Colas por otro lado usa FIFO, el primero en llegar es el primero en salir
# Los dos son igual de utiles dependiendo del contexto que necesite, por esto es importante aprender la logica de los dos


class ColaPrioridadClientes: #Se crea la clase
    def __init__(self):  #Se inicia con init y self
        self.items=[]
    def agregar_cliente(self,nombre,prioridad):  #funcion que permite agregar clientes con su prioridad
        self.items.append((prioridad,nombre))
    def atender_clientes(self): #funcion que elimina los clientes ya atendidos de la lista en base a su prioridad
        if not self.items:
            print('No hay clientes por atender')
        else:
            self.items.sort(key=lambda x: x[0])
            paciente_atentdido=self.items.pop(0)
            print('Se atendio a',paciente_atentdido[1])
            print('Siguiente porfavor')
    def mostrar_pendientes(self):  # recorre la lista de clientes que hay por atender, en caso de haber se imprime un mensaje
        if not self.items:
            print('No hay mas clientes')
        else:
            for prioridad,clientes in self.items:
                print(clientes,'con prioridad: ',prioridad)
    def tamano(self):  #funcion que permite saber el largo de la lista
        print('Estan',len(self.items),'a la cola para ser atendidos')

def continuar():  #funcion extra para que el codigo sea mas agradable a la vista
    input('Presione enter para continuar...')

clientes=ColaPrioridadClientes()


#se agrega los 8 primeros clientes
clientes.agregar_cliente('Adrian',3)  
clientes.agregar_cliente('David',1)
clientes.agregar_cliente('Angela',2)
clientes.agregar_cliente('Sebastian',4)
clientes.agregar_cliente('Carla',1)
clientes.agregar_cliente('Alicia',1)
clientes.agregar_cliente('Esteban',4)
clientes.agregar_cliente('Carlos',3)


#menu principal
while True:
    print('\nMenu de opciones\n')
    print('1. Agregar clientes')
    print('2. Atender clientes')
    print('3. Mostrar clientes pendientes')
    print('4. Mostrar tamano de la cola')
    print('5. Salir')
    opcion=int(input('Elija una opcion: '))
    if opcion==1:
        cliente_nuevo=input('Ingrese el nombre del cliente: ')
        prioridad_nueva=int(input('Ingrese la prioridad: '))
        clientes.agregar_cliente(cliente_nuevo,prioridad_nueva)
        print('Se agrego',cliente_nuevo,'con prioridad',prioridad_nueva)
        continuar()
    elif opcion==2:
        clientes.atender_clientes()
        continuar()
    elif opcion==3:
        clientes.mostrar_pendientes()
        continuar()
    elif opcion==4:
        clientes.tamano()
        continuar()
    elif opcion==5:
        print('Gracias por usar el programa...')
        break
    else:
        print('Opcion invalida')
        continuar()
