from pacientes import Paciente

pacientes= []

def registrar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = int(input("Ingrese la edad del paciente: "))
    cedula = int(input('Ingrese la cedula del paciente: '))
    sangre = input('Ingrese el tipo de sange: ')
    paciente = Paciente(nombre, cedula, edad, sangre)
    pacientes.append(paciente)

def buscar_paciente(cedula):
    for paciente in pacientes:
        if paciente.cedula == cedula:
            return paciente
    return None


def registrar_consulta():
    cedulan = int(input("Ingrese la cedula del paciente: "))
    paciente = buscar_paciente(cedulan)
    if paciente:
        fecha = input('Ingrese la fecha de la consulta: ')
        diagnostico = input('Ingrese el diagnostico: ')
        tratamiento = input('Ingrese el tratamiento: ')
        paciente.agregar_consulta(fecha, diagnostico, tratamiento)
        print('Consulta registrada con exito')
    else:
        print('Paciente no registrado')
            





def mostrar_datos():
    cedula = int(input('Ingrese la cedula del paciente: '))
    paciente = buscar_paciente(cedula)
    if paciente:
        paciente.mostrar_datos()
    else:
        print('Paciente no encontrado')


def mostrar_todo():
    if not pacientes:
        print('No hay pacientes reggstrados')
    else:
        for paciente in pacientes:
            paciente.mostrar_datos()
