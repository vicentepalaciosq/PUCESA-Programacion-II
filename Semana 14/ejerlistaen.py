#Hecho por: Vicente Palacios

class NodoSimple:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.actual = None  

    def insertar(self, dato):
        elemento = NodoSimple(dato)
        if not self.cabeza:
            self.cabeza = elemento
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = elemento

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end='->')
            actual = actual.siguiente
        print('Final')

    def eliminar(self, elemento):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato == elemento:
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return
            anterior = actual
            actual = actual.siguiente
        print('Elemento', elemento, 'no encontrado')

    def reiniciar(self):
        self.actual = self.cabeza

    def avanzar(self):
        if self.actual is None:
            self.reiniciar()
            if self.actual:
                print('Elemento actual:', self.actual.dato)
            else:
                print('La fila está vacía.')
        elif self.actual.siguiente:
            self.actual = self.actual.siguiente
            print('Avanzando... Elemento actual:', self.actual.dato)
        else:
            print('Final')


fila = ListaSimple()
fila.insertar('Vicente')
fila.insertar('Maria')
fila.insertar('Andrea')
fila.insertar('Paula')
fila.insertar('Adrian')


def enter():
    input('Presione enter para continuar...')  

def mostrar_menu():
    while True:
        print("\n\tFila de atencion\n\t")
        print('\n\tMenu de opciones\n\t')
        print('1. Agregar a la fila')
        print('2. Mostrar la fila')
        print('3. Eliminar al primero de la fila')
        print('4. Avanzar la fila')
        print('5. Salir')
        try:
            opcion = int(input('Ingrese una opcion: '))
        except ValueError:
            print('Debe ingresar un número')
            enter()
            continue

        if opcion == 1:
            dato = input('Ingrese el nombre de la persona que va a agregar: ')
            fila.insertar(dato)
            print(dato, 'se encuentra al final de la fila')
            enter()
        elif opcion == 2:
            print('\t\nFila de atencion')
            fila.mostrar()
            enter()
        elif opcion == 3:
            dato = input('Ingrese el nombre de la persona que va a eliminar de la fila: ')
            fila.eliminar(dato)
            enter()
        elif opcion == 4:
            fila.avanzar()
            enter()
        elif opcion == 5:
            print('Gracias por usar el programa!')
            break
        else:
            print('Elija una opcion valida')
            enter()

mostrar_menu()
