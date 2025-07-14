#Hecho por: Vicente Palacios
#Fecha: 16/06/25
#Parte 1



# Reflexion final
# Explica en tus propias palabras: ¿Qué diferencias observas entre el funcionamiento de una PILA y una COLA CON PRIORIDAD?

# Pilas y colas al principio parecen lo mismo, ademas de servir para mantener un orden, usan distintos principios
# Pilas por un lado usa LIFO que significa que el ultimo que llega es el primero que sale
# Colas por otro lado usa FIFO, el primero en llegar es el primero en salir
# Los dos son igual de utiles dependiendo del contexto que necesite, por esto es importante aprender la logica de los dos

class PilaTareas:  #creacion de la clase
    def __init__(self):  #se inicia con init y self
        self.items=[]
    def agregar_tarea(self,tarea): #funcion que permite agregar tareas a la lista
        self.items.append(tarea)
        
        return tarea
    def terminar_tarea(self):  #funcion que elimina la ultima tarea, en caso de no haber taresa se imprime unn mensaje
        if not self.items:
            print('Ya no hay tareas a realizarse')
        else:
            
            tarea_terminada=self.items.pop()
            print('Se completo la tarea:',tarea_terminada)
    
    def ver_ultima_tarea(self):  #funcion que imprime la siguiente tarea que se va a realizar
        if not self.items:
            print('Ya no hay tareas a realizarse')
        else:
            print('Tarea a realizarse:',self.items[-1])
    
    def tamano(self):  #funcion que imprime el largo de la lista
        print('Faltan',len(self.items),'tareas por completar')

tareas=PilaTareas()

#se agregan 10 primeras tareas

tareas.agregar_tarea('Revisar correos electrónicos')
tareas.agregar_tarea("Llamar al cliente para seguimiento")
tareas.agregar_tarea("Actualizar base de datos de inventario")
tareas.agregar_tarea("Redactar informe semanal")
tareas.agregar_tarea("Asistir a reunión de equipo")
tareas.agregar_tarea("Configurar equipo nuevo")
tareas.agregar_tarea("Capacitar a nuevo empleado")
tareas.agregar_tarea("Organizar archivos del proyecto")
tareas.agregar_tarea("Responder consultas del chat interno")
tareas.agregar_tarea("Preparar presentación mensual")

def continuar():  #funcion para que el codigo sea mas agradable
    input('Presione enter para continuar...')

#menu principal

while True:
    print('\nMenu de opciones\n')
    print('1. Agregar tarea')
    print('2. Terminar tarea')
    print('3. Ver ultima tarea')
    print('4. Ver cuantas tareas faltan')
    opcion=int(input('\nElija una opcion: '))
    if opcion==1:
        tarea_nueva=input('Ingrese una nueva tarea: ')
        print('Se agrego',tarea_nueva,'a la lista de tareas')
        tareas.agregar_tarea(tarea_nueva)
        continuar()
    elif opcion==2:
        tareas.terminar_tarea()
        continuar()
    elif opcion==3:
        tareas.ver_ultima_tarea()
        continuar()
    elif opcion==4:
        tareas.tamano()
        continuar()
    elif opcion==5:
        print('Gracias por usar el programa!')
        break
    else:
        print('Opcion invalida...')
        continuar()