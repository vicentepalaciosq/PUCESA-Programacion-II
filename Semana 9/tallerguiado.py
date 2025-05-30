# Taller Guiado: Métodos de Ordenamiento Clásicos en Python

# 1. Bubble Sort (Ordenamiento burbuja)
def bubble_sort(lista):
    n = len(lista)  # Guardamos la longitud de la lista

    # Recorremos toda la lista n veces
    for i in range(n):
        # En cada pasada, comparamos elementos adyacentes
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambiamos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                # Intercambio usando desempaquetado de tuplas

    return lista  # Retornamos la lista ordenada

# Prueba
numeros = [5, 2, 9, 1, 7]
print("Original:", numeros)
print("Ordenado:", bubble_sort(numeros.copy()))

# 2. Insertion Sort (Ordenamiento por inserción)
def insertion_sort(lista):
    # Recorremos desde el segundo elemento hasta el final
    for i in range(1, len(lista)):
        actual = lista[i]  # Elemento actual a insertar
        j = i - 1          # Posición anterior

        # Mientras haya elementos mayores que el actual, los movemos una posición a la derecha
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1

        # Insertamos el elemento en su posición correcta
        lista[j + 1] = actual

    return lista  # Retornamos la lista ordenada

# Prueba
numeros = [5, 2, 9, 1, 7]
print("Original:", numeros)
print("Ordenado:", insertion_sort(numeros.copy()))

# 3. Selection Sort (Ordenamiento por selección)
def selection_sort(lista):
    n = len(lista)

    # Recorremos todos los elementos
    for i in range(n):
        min_idx = i  # Suponemos que el mínimo está en la posición actual

        # Buscamos el menor elemento en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j  # Actualizamos el índice del nuevo mínimo

        # Si encontramos un nuevo mínimo, lo intercambiamos con el actual
        if min_idx != i:
            lista[i], lista[min_idx] = lista[min_idx], lista[i]

    return lista

# Prueba
numeros = [5, 2, 9, 1, 7]
print("Original:", numeros)
print("Ordenado:", selection_sort(numeros.copy()))
