# Ejercicio 1

def bus_lineal(lista, objetivo):
    contador = 0  
    for i in range(len(lista)):  # Recorre toda la lista
        contador += 1  # Aumenta el contador por cada comparacion
        if lista[i] == objetivo.lower():  # Compara el elemento con el objetivo 
            return i, contador  # Si lo encuentra retorna su posicion y numero de comparaciones
    return -1, contador  # Si no lo encuentra retorna -1 y el numero de comparaciones realizadas


frutas = ["manzana", "banana", "naranja", "uva", "guanabana", "mango", "pera", "piña", "cereza", "frutilla"]
buscar = input("Ingrese el nombre de la fruta a buscar: ")
pos, comparaciones = bus_lineal(frutas, buscar)

# Resultado 
if pos != -1:
    print(buscar, "se encontró en la posición", pos)
else:
    print(buscar, "no se encontró en la lista")
# Muestra cauntas comparaciones se hicieron
print("Se hicieron", comparaciones, "comparaciones")




#Ejercicio 2

def busqueda_binaria(lista, objetivo):
    inicio = 0  # Límite inferior 
    fin = len(lista) - 1  # Límite superior 
    contador = 0  

    while inicio <= fin:  # Valida que el rango de búsqueda sea valido
        medio = (inicio + fin) // 2  # Calcula la posicion media del rango
        contador += 1  # Aumenta el contador por cada comparación
        if lista[medio] == objetivo:  # Encuentra el objetivo
            return medio, contador  # Retorna  posición y comparaciones 
        elif lista[medio] < objetivo:  
            inicio = medio + 1
        else:  
            fin = medio - 1
    return -1, contador  # Si no lo encuentra retorna -1 y las comparaciones 


numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
buscar = int(input("Ingrese el número a buscar: "))
pos, cont = busqueda_binaria(numeros, buscar)

# Resultado 
if pos != -1:
    print(buscar, "se encontró en la posición", pos)
else:
    print(buscar, "no se encontró en la lista")

# Mostrar cuantas comparaciones se hicieron
print("Se hicieron", cont, "comparaciones")
