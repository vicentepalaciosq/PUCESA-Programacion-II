#Hecho por: Vicente Palacios

class ReporteMedico:
    def __init__(self, tipo, observacion):
        self.tipo = tipo
        self.observacion = observacion

class PilaReportes:
    def __init__(self):
        self.reportes = []  

    def agregar_reporte(self, tipo, observacion):
        reporte = ReporteMedico(tipo, observacion)
        self.reportes.append(reporte)
        print("Reporte agregado:", tipo, "-", observacion)

    def eliminar_reporte(self):
        if not self.reportes:
            print('No existen mas reportes')
        else:
            eliminado = self.reportes.pop()
            print('Se elimino el reporte:', eliminado.tipo, 'con observacion:', eliminado.observacion)

    def mostrar_reportes(self):
        if not self.reportes:
            print("No hay reportes para mostrar.")
        else:
            print("Reportes actuales:")
            for reporte in self.reportes:
                print('Tipo:', reporte.tipo, '| Observacion:', reporte.observacion)

class EstudianteEvacuacion:
    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula

class NodoCola:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None

class ColaEvacuacion:
    def __init__(self):
        self.frente = None
        self.final = None

    def agregar_estudiante(self, nombre, aula):
        nuevo_estudiante = EstudianteEvacuacion(nombre, aula)
        nodo = NodoCola(nuevo_estudiante)
        if self.frente is None:
            self.frente = self.final = nodo
        else:
            self.final.siguiente = nodo
            self.final = nodo
        print("Estudiante agregado a evacuacion:", nombre, "- Aula:", aula)

    def atender_estudiante(self):
        if self.frente is None:
            print("No hay estudiantes en la cola.")
        else:
            atendido = self.frente.estudiante
            self.frente = self.frente.siguiente
            if self.frente is None:
                self.final = None
            print("Estudiante evacuado:", atendido.nombre, "- Aula:", atendido.aula)

    def mostrar_en_espera(self):
        if self.frente is None:
            print("No hay estudiantes en espera.")
        else:
            actual = self.frente
            print("Estudiantes en espera:")
            while actual:
                print("-", actual.estudiante.nombre, "(Aula:", actual.estudiante.aula, ")")
                actual = actual.siguiente

class VisitaMedica:
    def __init__(self, estudiante, motivo, fecha):
        self.estudiante = estudiante
        self.motivo = motivo
        self.fecha = fecha

class NodoDoble:
    def __init__(self, visita):
        self.visita = visita
        self.anterior = None
        self.siguiente = None

class ListaVisitas:
    def __init__(self):
        self.actual = None

    def agregar_visita(self, estudiante, motivo, fecha):
        nueva_visita = VisitaMedica(estudiante, motivo, fecha)
        nodo = NodoDoble(nueva_visita)
        if self.actual is None:
            self.actual = nodo
        else:
            nodo.anterior = self.actual
            self.actual.siguiente = nodo
            self.actual = nodo
        print("Visita medica registrada:", estudiante, "-", motivo, "-", fecha)

    def retroceder(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            self.mostrar_actual()
        else:
            print("No hay visitas anteriores.")

    def avanzar(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            self.mostrar_actual()
        else:
            print("No hay visitas siguientes.")

    def mostrar_actual(self):
        if self.actual:
            actual = self.actual.visita
            print("Visita actual:", actual.estudiante, "-", actual.motivo, "-", actual.fecha)
        else:
            print("No hay visitas registradas.")

class Incidente:
    def __init__(self, anio, tipo):
        self.anio = anio
        self.tipo = tipo

class NodoIncidente:
    def __init__(self, incidente):
        self.incidente = incidente
        self.siguiente = None

class ListaBitacora:
    def __init__(self):
        self.inicio = None

    def agregar_incidente(self, anio, tipo):
        nuevo_incidente = NodoIncidente(Incidente(anio, tipo))
        if self.inicio is None:
            self.inicio = nuevo_incidente
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_incidente
        print("Incidente registrado:", anio, "-", tipo)

    def eliminar_incidente(self, anio):
        actual = self.inicio
        anterior = None
        while actual:
            if actual.incidente.anio == anio:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente
                print("Incidente del anio", anio, "eliminado.")
                return
            anterior = actual
            actual = actual.siguiente
        print("Incidente del anio", anio, "no encontrado.")

    def buscar_incidente(self, anio):
        actual = self.inicio
        while actual:
            if actual.incidente.anio == anio:
                print("Incidente encontrado:", actual.incidente.anio, "-", actual.incidente.tipo)
                return
            actual = actual.siguiente
        print("Incidente del anio", anio, "no encontrado.")

    def mostrar_incidentes(self):
        if self.inicio is None:
            print("No hay incidentes registrados.")
        else:
            actual = self.inicio
            print("Bitacora de incidentes:")
            while actual:
                print(actual.incidente.anio, "-", actual.incidente.tipo)
                actual = actual.siguiente


pila = PilaReportes()
cola = ColaEvacuacion()
visitas = ListaVisitas()
bitacora = ListaBitacora()

while True:
    print('\n\tMenu de Opciones\n\t')
    print('1. Reportes medicos estudiantiles')
    print('2. Evacuacion escolar simulada')
    print('3. Registro de visitas al departamento medico')
    print('4. Bitacora de incidentes escolares')
    print('5. Salir')
    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        while True:
            print('\n Reportes Medicos ')
            print('1. Agregar reporte')
            print('2. Eliminar reporte')
            print('3. Mostrar reportes')
            print('4. Volver al menu principal')
            op = int(input('Ingrese una opcion: '))
            if op == 1:
                tipo = input('Tipo de reporte: ')
                observacion = input('Observacion: ')
                pila.agregar_reporte(tipo, observacion)
            elif op == 2:
                pila.eliminar_reporte()
            elif op == 3:
                pila.mostrar_reportes()
            elif op == 4:
                break

    elif opcion == 2:
        while True:
            print('\n Simulacion de Evacuacion ')
            print('1. Agregar estudiante a la cola')
            print('2. Atender estudiante')
            print('3. Mostrar estudiantes en espera')
            print('4. Volver al menu principal')
            op = int(input('Ingrese una opcion: '))
            if op == 1:
                nombre = input('Nombre del estudiante: ')
                aula = input('Aula: ')
                cola.agregar_estudiante(nombre, aula)
            elif op == 2:
                cola.atender_estudiante()
            elif op == 3:
                cola.mostrar_en_espera()
            elif op == 4:
                break

    elif opcion == 3:
        while True:
            print('\n Registro de Visitas Medicas ')
            print('1. Agregar visita')
            print('2. Retroceder')
            print('3. Avanzar')
            print('4. Mostrar visita actual')
            print('5. Volver al menu principal')
            op = int(input('Ingrese una opcion: '))
            if op == 1:
                estudiante = input('Nombre del estudiante: ')
                motivo = input('Motivo: ')
                fecha = input('Fecha: ')
                visitas.agregar_visita(estudiante, motivo, fecha)
            elif op == 2:
                visitas.retroceder()
            elif op == 3:
                visitas.avanzar()
            elif op == 4:
                visitas.mostrar_actual()
            elif op == 5:
                break

    elif opcion == 4:
        while True:
            print('\n Bitacora de Incidentes ')
            print('1. Agregar incidente')
            print('2. Eliminar incidente')
            print('3. Buscar incidente')
            print('4. Mostrar todos los incidentes')
            print('5. Volver al menu principal')
            op = int(input('Ingrese una opcion: '))
            if op == 1:
                anio = input('Anio del incidente: ')
                tipo = input('Tipo de incidente: ')
                bitacora.agregar_incidente(anio, tipo)
            elif op == 2:
                anio = input('Anio del incidente a eliminar: ')
                bitacora.eliminar_incidente(anio)
            elif op == 3:
                anio = input('Anio del incidente a buscar: ')
                bitacora.buscar_incidente(anio)
            elif op == 4:
                bitacora.mostrar_incidentes()
            elif op == 5:
                break

    elif opcion == 5:
        print('Saliendo del sistema...')
        break
    else:
        print('Opcion no valida.')

