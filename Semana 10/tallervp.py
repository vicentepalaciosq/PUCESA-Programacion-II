# Hecho por: Vicente Palacios


# ¿Qué método te pareció más eficiente o claro para ordenar?
#El método que me pareció más eficiente y claro para ordenar fue el uso de sorted(), 
# ya que es rápido, directo y fácil de usar. Aunque no muestra cómo funciona internamente

# ¿Crees que es útil visualizar el proceso de ordenamiento?
#Visualizar el proceso de ordenamiento fue muy útil, ya que convierte un concepto abstracto en algo visual. 
#Observar el movimiento de las barras permite identificar patrones para entender mejor la eficiencia de los métodos



import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import bisect


notas = random.sample(range(0, 21), 15)
print("Notas originales:", notas)


resultados = []

def animar_comparacion_sorted_bubble_simulada(lista_original, pausa=0.3):
    # Copias de trabajo
    lista_bubble = lista_original.copy()
    pasos_bubble = [lista_bubble.copy()]
    n = len(lista_bubble)


    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_bubble[j] > lista_bubble[j + 1]:
                lista_bubble[j], lista_bubble[j + 1] = lista_bubble[j + 1], lista_bubble[j]
                pasos_bubble.append(lista_bubble.copy())


    lista_sorted_final = sorted(lista_original)
    lista_simulada = lista_original.copy()
    pasos_sorted = []

    for i in range(len(lista_sorted_final)):
        if lista_simulada[i] != lista_sorted_final[i]:
            lista_simulada[i] = lista_sorted_final[i]
        pasos_sorted.append(lista_simulada.copy())

    total_pasos = max(len(pasos_bubble), len(pasos_sorted))


    plt.ion()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))


    barras_bubble = ax1.bar(range(len(lista_original)), lista_original, color='skyblue')
    ax1.set_title("Bubble Sort - Paso 1")
    ax1.set_ylim(0, max(lista_original) + 5)

    barras_sorted = ax2.bar(range(len(lista_original)), lista_original, color='lightgreen')
    ax2.set_title("sorted() - Paso 1")
    ax2.set_ylim(0, max(lista_original) + 5)

    for k in range(total_pasos):
        # Bubble Sort
        if k < len(pasos_bubble):
            for rect, h in zip(barras_bubble, pasos_bubble[k]):
                rect.set_height(h)
            ax1.set_title(f"Bubble Sort - Paso {k + 1}")
        else:
            for rect, h in zip(barras_bubble, pasos_bubble[-1]):
                rect.set_height(h)
            ax1.set_title("Bubble Sort - Final")


        if k < len(pasos_sorted):
            for rect, h in zip(barras_sorted, pasos_sorted[k]):
                rect.set_height(h)
            ax2.set_title(f"sorted() - Paso {k + 1}")
        else:
            for rect, h in zip(barras_sorted, lista_sorted_final):
                rect.set_height(h)
            ax2.set_title("sorted() - Final")

        plt.pause(pausa)

    plt.ioff()
    plt.show()


    print("Notas ordenadas:", lista_sorted_final)
    

nueva_nota = int(input('Ingrese una nueva nota: '))
bisect.insort(notas, nueva_nota)
print(" Lista después de insertar la nueva nota:", notas)

nota_buscar = int(input('Ingrese una nota a buscar: '))  
posicion = bisect.bisect_left(notas, nota_buscar)
if posicion < len(notas) and notas[posicion] == nota_buscar:
    print(f"🔍 La nota {nota_buscar} se encuentra en la posición {posicion}")
else:
    print(f"❌ La nota {nota_buscar} no está en la lista.")


animar_comparacion_sorted_bubble_simulada(notas)
