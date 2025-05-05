class Paciente:
    def __init__(self, nombre, cedula, edad, sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.sangre = sangre
        self.consultas = []

    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        consulta = {
            "fecha": fecha,
            "diagnostico": diagnostico,
            "tratamiento": tratamiento
        }
        self.consultas.append(consulta)

    def mostrar_datos(self):
        print('Nombre:', self.nombre)
        print('Cedula:', self.cedula)
        print('Edad: ', self.edad)
        print('Tipo de sangre:', self.sangre)
        if len(self.consultas) > 0:
            print("Historial de consultas:")
            for consulta in self.consultas:
                print("  Fecha:", consulta['fecha'])
                print("  Diagnostico:", consulta['diagnostico'])
                print("  Tratamiento:", consulta['tratamiento'])
        else:
            print("Sin consultas")

