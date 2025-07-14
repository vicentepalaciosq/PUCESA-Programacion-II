#Hecho por: Vicente Palacios

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.actual = None

    def insertar(self, dato):
        elemento = NodoDoble(dato)
        if not self.cabeza:
            self.cabeza = elemento
            self.actual = elemento
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = elemento
            elemento.anterior = actual
            self.actual = elemento

    def mostrar(self):
        actual = self.cabeza
        print('\nHistorial de Navegacion:')
        while actual:
            if actual == self.actual:
                print('[', actual.dato, ']', end=' <-> ')
            else:
                print(actual.dato, end=' <-> ')
            actual = actual.siguiente
        print('Null')

    def mostrar_atras(self):
        actual = self.actual
        while actual and actual.siguiente:
            actual = actual.siguiente
        print('\nNavegación desde el final:')
        while actual:
            if actual == self.actual:
                print('[', actual.dato, ']', end=' <-> ')
            else:
                print(actual.dato, end=' <-> ')
            actual = actual.anterior
        print('Null')

    def avanzar(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            print('Moviendo adelante... ahora estás en:', self.actual.dato)
        else:
            print('No hay mas paginas adelante')

    def retroceder(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            print('Yendo hacia atras... ahora visitando:', self.actual.dato)
        else:
            print('Ya estás en la primera pagina.')

    def eliminar_actual(self):
        if not self.actual:
            print('No hay pagina actual para elimina')
            return
        if self.actual.anterior:
            self.actual.anterior.siguiente = self.actual.siguiente
        else:
            self.cabeza = self.actual.siguiente
        if self.actual.siguiente:
            self.actual.siguiente.anterior = self.actual.anterior
        temp = self.actual
        self.actual = self.actual.siguiente if self.actual.siguiente else self.actual.anterior
        print('Eliminaste la pagina:', temp.dato)

def enter():
    input('Presione enter para continuar...')

def mostrar_menu():
    navegador = ListaDoble()
    navegador.insertar('youtube.com')
    navegador.insertar('chatgpt.com')
    navegador.insertar('wikipedia.com')
    navegador.insertar('google.com')
    navegador.insertar('facebook.com')
    while True:
        print("\n\tNavegador Web\n\t")
        print('\n\tMenú de opciones\n\t')
        print('1. Visitar nueva pagina')
        print('2. Mostrar historial')
        print('3. Mostrar desde el final')
        print('4. Avanzar')
        print('5. Retroceder')
        print('6. Eliminar pagina actual')
        print('7. Salir')
        try:
            opcion = int(input('Ingrese una opción: '))
        except ValueError:
            print('Debe ingresar un número.')
            enter()
            continue

        if opcion == 1:
            url = input('Ingrese la URL de la pagina: ')
            navegador.insertar(url)
            print(url, 'fue visitada.')
            enter()
        elif opcion == 2:
            navegador.mostrar()
            enter()
        elif opcion == 3:
            navegador.mostrar_atras()
            enter()
        elif opcion == 4:
            navegador.avanzar()
            enter()
        elif opcion == 5:
            navegador.retroceder()
            enter()
        elif opcion == 6:
            navegador.eliminar_actual()
            enter()
        elif opcion == 7:
            print('Gracias por usar el navegador!')
            break
        else:
            print('Elija una opción valida')
            enter()



mostrar_menu()
