#Hecho por: Vicente Palacios

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None

class HistorialNavegador:
    def __init__(self):
        self.historial = ListaDobleEnlazada()
        self.actual = None

    def visitar_pagina(self, url):
        nuevo = NodoDoble(url)
        if self.actual is None:
            self.historial.cabeza = nuevo
            self.actual = nuevo
        else:
            self.actual.siguiente = None
            nuevo.anterior = self.actual
            self.actual.siguiente = nuevo
            self.actual = nuevo
        print("Visitando:", url)

    def atras(self):
        if self.actual is not None and self.actual.anterior is not None:
            self.actual = self.actual.anterior
            print("Volviendo a:", self.actual.dato)
        else:
            print("No hay pagina anterior")

    def adelante(self):
        if self.actual is not None and self.actual.siguiente is not None:
            self.actual = self.actual.siguiente
            print("Avanzando a:", self.actual.dato)
        else:
            print("No hay pagina siguiente")

    def mostrar_historial(self):
        actual = self.historial.cabeza
        print("Historial completo:")
        while actual is not None:
            marcador = "<- Actual" if actual == self.actual else ""
            print(actual.dato, marcador)
            actual = actual.siguiente

    def pagina_actual(self):
        if self.actual is not None:
            print("Pagina actual:", self.actual.dato)
        else:
            print("No se ha visitado ninguna pagina.")

def enter():
    input('Presione enter para continuar...')

navegador = HistorialNavegador()
navegador.visitar_pagina('google.com')
navegador.visitar_pagina('youtube.com')
navegador.visitar_pagina('netflix.com')



while True:
    print('\n Menu de opciones\n')
    print('1. Visitar nueva pagina')
    print('2. Ir atras')
    print('3. Ir adelante')
    print('4. Mostrar historial')
    print('5. Mostrar pagina actual')
    print('6. Salir')
    opcion=int(input('Ingrese una opcion: '))
    if opcion==1:
        url=input('Ingrese la pagina: ')
        navegador.visitar_pagina(url)
        enter()
    elif opcion==2:
        navegador.atras()
        enter()
    elif opcion==3:
        navegador.adelante()
        enter()
    elif opcion==4:
        navegador.mostrar_historial()
        enter()
    elif opcion==5:
        navegador.pagina_actual()
        enter()
    elif opcion==6:
        print('Gracias por usar el programa!')
        break
    else:
        print('Elija una opcion valida')
        enter()