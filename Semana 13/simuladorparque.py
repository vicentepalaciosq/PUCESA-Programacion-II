#Hecho por Vicente Palacios

from collections import deque
import time
import random

cola_general = deque()
cola_prioritaria = deque()
cola_discapacidad = deque()

total_atendidos = 0
total_general = 0
total_prioritaria = 0
total_discapacidad = 0
viajes_realizados = 0

CAPACIDAD_VAGON = 4
DURACION_VIAJE = 3


def agregar_visitante(nombre, tipo="general"):
    global total_general, total_prioritaria, total_discapacidad
    if tipo == "discapacidad":
        cola_discapacidad.append(nombre)
        total_discapacidad += 1
    elif tipo == "prioritaria":
        cola_prioritaria.append(nombre)
        total_prioritaria += 1
    else:
        cola_general.append(nombre)
        total_general += 1


def mostrar_colas():
    print('\nCola Discapacidad:', list(cola_discapacidad))
    print('Cola Prioritaria:', list(cola_prioritaria))
    print('Cola General:', list(cola_general))


def cargar_vagon():
    pasajeros = []
    while len(pasajeros) < CAPACIDAD_VAGON:
        if cola_discapacidad:
            pasajeros.append((cola_discapacidad.popleft(), "Discapacidad"))
        elif cola_prioritaria:
            pasajeros.append((cola_prioritaria.popleft(), "Prioridad"))
        elif cola_general:
            pasajeros.append((cola_general.popleft(), "General"))
        else:
            break
    return pasajeros


def generar_ticket(nombre, tipo, viaje):
    print(f"\n--- TICKET ---")
    print(f"Nombre: {nombre}")
    print(f"Tipo de acceso: {tipo}")
    print(f"Número de viaje: {viaje}")
    print("¡Gracias por visitar K-Boom Park!")
    print(f"----------------\n")


def simular_viaje(pasajeros, numero_viaje, espera):
    global total_atendidos, viajes_realizados
    print(f"\nViaje #{numero_viaje} con: {[nombre for nombre, _ in pasajeros]}")
    for nombre, tipo in pasajeros:
        generar_ticket(nombre, tipo, numero_viaje)
    for i in range(DURACION_VIAJE):
        print(f"Turno {i+1}/{DURACION_VIAJE}")
        time.sleep(espera)
    total_atendidos += len(pasajeros)
    viajes_realizados += 1
    print("\nViaje finalizado!\n")


def mostrar_estadisticas():
    print("\n=== Estadísticas Finales ===")
    print(f"Total de personas atendidas: {total_atendidos}")
    print(f" - General: {total_general}")
    print(f" - Prioritaria: {total_prioritaria}")
    print(f" - Discapacidad: {total_discapacidad}")
    if viajes_realizados:
        print(f"Promedio de personas por viaje: {total_atendidos / viajes_realizados:.2f}")
    else:
        print("No se realizaron viajes.")

tipo_acceso = {"1": "general", "2": "prioritaria", "3": "discapacidad"}
espera = int(input("\nIngresa el tiempo de espera entre turnos (en segundos): "))
numero_viaje = 1

while True:
    print("\n--- Menú ---")
    print("1. Agregar persona")
    print("2. Ver estado de las colas")
    print("3. Simular viaje")
    print("4. Salir del sistema")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la persona: ")
        print("Tipo de acceso: 1. General  2. Prioridad  3. Discapacidad")
        tipo_op = input("Seleccione el tipo (1-3): ")
        tipo = tipo_acceso.get(tipo_op, "general")
        agregar_visitante(nombre, tipo)

    elif opcion == "2":
        mostrar_colas()

    elif opcion == "3":
        if len(cola_general) + len(cola_prioritaria) + len(cola_discapacidad) >= CAPACIDAD_VAGON:
            pasajeros = cargar_vagon()
            simular_viaje(pasajeros, numero_viaje, espera)
            numero_viaje += 1
        else:
            print("\nAún no hay suficientes personas para el viaje")

    elif opcion == "4":
        mostrar_estadisticas()
        print("\nGracias por usar el sistema de simulación K-Boom Park!")
        break

    else:
        print("\nOpción no válida. Intente de nuevo.")
