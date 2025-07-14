#  _ _____                _  
# (_)_   _| _ __ _ ___ __| |
# | | | || '_/ _` / -_) _` |
# |_| |_||_| \__,_\___\__,_|
#         ̶J̶o̶s̶h̶u̶a̶ ̶J̶a̶c̶o̶m̶e̶

# Clase ReporteMedico
class ReporteMedico:
    def __init__(self, tipo, observacion):
        self.tipo = tipo
        self.observacion = observacion

# Clase PilaReportes
class PilaReportes:
    def __init__(self):
        self.reportes = []  # Lista que almacena los reportes

    def agregarReporte(self, tipo, observacion):
        reporte = ReporteMedico(tipo, observacion)
        self.reportes.append(reporte)  # Agregar reporte a la pila

    def eliminarReporte(self):
        if self.reportes:
            print(f"Eliminando reporte: {self.reportes[-1].tipo}")
            self.reportes.pop()  # Eliminar el último reporte de la pila
        else:
            print("No hay reportes para eliminar.")

    def mostrarReportes(self):
        if self.reportes:
            for reporte in self.reportes:
                print(f"Tipo: {reporte.tipo}, Observación: {reporte.observacion}")
        else:
            print("No hay reportes registrados.")

# Clase EstudianteEvacuacion
class EstudianteEvacuacion:
    def __init__(self, nombre, aula):
        self.nombre = nombre
        self.aula = aula

# Clase ColaEvacuacion
class ColaEvacuacion:
    def __init__(self):
        self.estudiantes = []  # Lista que almacena los estudiantes en espera

    def agregarEstudiante(self, nombre, aula):
        estudiante = EstudianteEvacuacion(nombre, aula)
        self.estudiantes.append(estudiante)  # Agregar estudiante a la cola

    def atenderEstudiante(self):
        if self.estudiantes:
            estudiante = self.estudiantes.pop(0)  # Atender al primer estudiante
            print(f"Atendiendo al estudiante: {estudiante.nombre}")
        else:
            print("No hay estudiantes para atender.")

    def mostrarEnEspera(self):
        if self.estudiantes:
            for estudiante in self.estudiantes:
                print(f"Estudiante: {estudiante.nombre}, Aula: {estudiante.aula}")
        else:
            print("No hay estudiantes en espera.")

# Clase VisitaMedica
class VisitaMedica:
    def __init__(self, estudiante, motivo, fecha):
        self.estudiante = estudiante
        self.motivo = motivo
        self.fecha = fecha

# Nodo doble
class NodoDoble:
    def __init__(self, visita):
        self.visita = visita
        self.anterior = None
        self.siguiente = None

# Clase ListaVisitas
class ListaVisitas:
    def __init__(self):
        self.actual = None

    def agregarVisita(self, estudiante, motivo, fecha):
        visita = VisitaMedica(estudiante, motivo, fecha)
        nodo = NodoDoble(visita)
        if self.actual is None:
            self.actual = nodo
        else:
            # Navegar hasta el último nodo
            actual_nodo = self.actual
            while actual_nodo.siguiente:
                actual_nodo = actual_nodo.siguiente
            actual_nodo.siguiente = nodo
            nodo.anterior = actual_nodo

    def retroceder(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
        else:
            print("No hay página anterior.")

    def avanzar(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
        else:
            print("No hay página siguiente.")

    def mostrarActual(self):
        if self.actual:
            print(f"Estudiante: {self.actual.visita.estudiante}, Motivo: {self.actual.visita.motivo}, Fecha: {self.actual.visita.fecha}")
        else:
            print("No hay visitas registradas.")

# Clase Incidente
class Incidente:
    def __init__(self, anio, tipo):
        self.anio = anio
        self.tipo = tipo

# Nodo simple
class NodoIncidente:
    def __init__(self, incidente):
        self.incidente = incidente
        self.siguiente = None

# Clase ListaBitacora
class ListaBitacora:
    def __init__(self):
        self.inicio = None

    def agregarIncidente(self, anio, tipo):
        incidente = Incidente(anio, tipo)
        nodo = NodoIncidente(incidente)
        if self.inicio is None:
            self.inicio = nodo
        else:
            # Navegar hasta el último nodo
            actual_nodo = self.inicio
            while actual_nodo.siguiente:
                actual_nodo = actual_nodo.siguiente
            actual_nodo.siguiente = nodo

    def eliminarIncidente(self, anio):
        actual_nodo = self.inicio
        anterior_nodo = None
        while actual_nodo and actual_nodo.incidente.anio != anio:
            anterior_nodo = actual_nodo
            actual_nodo = actual_nodo.siguiente
        if actual_nodo:
            if anterior_nodo:
                anterior_nodo.siguiente = actual_nodo.siguiente
            else:
                self.inicio = actual_nodo.siguiente

    def buscarIncidente(self, anio):
        actual_nodo = self.inicio
        while actual_nodo:
            if actual_nodo.incidente.anio == anio:
                return actual_nodo.incidente
            actual_nodo = actual_nodo.siguiente
        return None

    def mostrarIncidentes(self):
        actual_nodo = self.inicio
        while actual_nodo:
            print(f"Año: {actual_nodo.incidente.anio}, Tipo: {actual_nodo.incidente.tipo}")
            actual_nodo = actual_nodo.siguiente

# Menú interactivo
def menuPrincipal():
    print("**************  MENU PRINCIPAL  **************")
    print("1. Simular Reportes Médicos (Pilas)")
    print("2. Simular Evacuación Escolar (Colas)")
    print("3. Simular Visitas Médicas (Lista Doble)")
    print("4. Simular Bitácora de Incidentes (Lista Simple)")
    print("5. Salir")
    print("**********************************************")

def menuReportesMedicos():
    print("********** MENÚ Reportes Médicos **********")
    print("1. Agregar reporte médico")
    print("2. Eliminar reporte médico")
    print("3. Mostrar reportes médicos")
    print("4. Volver al menú principal")
    print("********************************************")

def menuEvacuacionEscolar():
    print("******** MENÚ Evacuación Escolar ********")
    print("1. Agregar estudiante a la evacuación")
    print("2. Atender estudiante")
    print("3. Mostrar estudiantes en espera")
    print("4. Volver al menú principal")
    print("******************************************")

def menuVisitasMedicas():
    print("********** MENÚ Visitas Médicas **********")
    print("1. Agregar visita médica")
    print("2. Retroceder")
    print("3. Avanzar")
    print("4. Mostrar visita actual")
    print("5. Volver al menú principal")
    print("********************************************")

def menuBitacoraIncidentes():
    print("****** MENÚ Bitácora de Incidentes ******")
    print("1. Agregar incidente")
    print("2. Eliminar incidente")
    print("3. Buscar incidente")
    print("4. Mostrar todos los incidentes")
    print("5. Volver al menú principal")
    print("******************************************")

# Función principal
def ejecutarSimulacion():
    pilaReportes = PilaReportes()
    colaEvacuacion = ColaEvacuacion()
    listaVisitas = ListaVisitas()
    listaBitacora = ListaBitacora()

    while True:
        menuPrincipal()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            while True:
                menuReportesMedicos()
                opcionReportes = input("Elige una opción: ")
                if opcionReportes == "1":
                    tipo = input("Ingresa el tipo de reporte: ")
                    observacion = input("Ingresa la observación: ")
                    pilaReportes.agregarReporte(tipo, observacion)
                elif opcionReportes == "2":
                    pilaReportes.eliminarReporte()
                elif opcionReportes == "3":
                    pilaReportes.mostrarReportes()
                elif opcionReportes == "4":
                    break
                else:
                    print("Opción no válida.")

        elif opcion == "2":
            while True:
                menuEvacuacionEscolar()
                opcionEvacuacion = input("Elige una opción: ")
                if opcionEvacuacion == "1":
                    nombre = input("Ingresa el nombre del estudiante: ")
                    aula = input("Ingresa el aula del estudiante: ")
                    colaEvacuacion.agregarEstudiante(nombre, aula)
                elif opcionEvacuacion == "2":
                    colaEvacuacion.atenderEstudiante()
                elif opcionEvacuacion == "3":
                    colaEvacuacion.mostrarEnEspera()
                elif opcionEvacuacion == "4":
                    break
                else:
                    print("Opción no válida.")

        elif opcion == "3":
            while True:
                menuVisitasMedicas()
                opcionVisitas = input("Elige una opción: ")
                if opcionVisitas == "1":
                    estudiante = input("Ingresa el nombre del estudiante: ")
                    motivo = input("Ingresa el motivo de la visita: ")
                    fecha = input("Ingresa la fecha de la visita: ")
                    listaVisitas.agregarVisita(estudiante, motivo, fecha)
                elif opcionVisitas == "2":
                    listaVisitas.retroceder()
                elif opcionVisitas == "3":
                    listaVisitas.avanzar()
                elif opcionVisitas == "4":
                    listaVisitas.mostrarActual()
                elif opcionVisitas == "5":
                    break
                else:
                    print("Opción no válida.")

        elif opcion == "4":
            while True:
                menuBitacoraIncidentes()
                opcionBitacora = input("Elige una opción: ")
                if opcionBitacora == "1":
                    anio = int(input("Ingresa el año del incidente: "))
                    tipo = input("Ingresa el tipo de incidente: ")
                    listaBitacora.agregarIncidente(anio, tipo)
                elif opcionBitacora == "2":
                    anio = int(input("Ingresa el año del incidente a eliminar: "))
                    listaBitacora.eliminarIncidente(anio)
                elif opcionBitacora == "3":
                    anio = int(input("Ingresa el año del incidente a buscar: "))
                    incidente = listaBitacora.buscarIncidente(anio)
                    if incidente:
                        print(f"Incidente encontrado: Año: {incidente.anio}, Tipo: {incidente.tipo}")
                    else:
                        print("Incidente no encontrado.")
                elif opcionBitacora == "4":
                    listaBitacora.mostrarIncidentes()
                elif opcionBitacora == "5":
                    break
                else:
                    print("Opción no válida.")
        
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamar a la función para iniciar la simulación
ejecutarSimulacion()