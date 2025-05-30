#Hecho por: Vicente Palacios
#Fecha: 26/05/25

#Como funciona cada algoritmo de ordenamiento?

#Bubble Sort 
# Compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Repite este proceso muchas veces hasta que la lista esté ordenada.

# Insertion Sort 
# Construye la lista ordenada insertando un elemento a la vez en su posición correcta. 

# Selection Sort 
# Busca el elemento más pequeño de la lista y lo coloca al inicio. Luego, repite este proceso con el resto de la lista. 

#Cual fue mas eficiente?
#De los tres algoritmos, Insertion Sort fue el más eficiente. Esto se notó porque hizo menos comparaciones e intercambios que los otros.
#Esto ocurre porque Insertion Sort es más rápido cuando la lista ya está en parte ordenada, como puede pasar con una lista de precios que no esté completamente desordenada. Solo mueve los elementos necesarios hasta dejarlos en su lugar correcto.

#En qué situaciones usarías cada uno en la vida real o en software?
# Insertion Sort es útil cuando tienes pocos datos o cuando los datos ya vienen casi ordenados.

# Bubble Sort no es recomendable para casos reales, pero sirve bien para aprender cómo funciona el ordenamiento, ya que es fácil de entender.

# Selection Sort puede ser útil cuando quieres minimizar los intercambios. Por ejemplo, si sw trabajara con memoria muy limitada 



precios= [

]

#Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    comparaciones=0
    intercambios=0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambios += 1

    return lista, comparaciones, intercambios


#Insertion Sort

def insertion_sort(lista):
    comparaciones = 0
    intercambios = 0
    for i in range(1, len(lista)):
        actual=lista[i]
        j= i - 1
        while j >= 0:
            comparaciones += 1
            if lista[j] > actual:
                lista[j + 1] = lista[j]
                j -= 1
                intercambios += 1
            else:
                break
        lista[j + 1] = actual

    return lista, comparaciones, intercambios




#Selection Sort
def selection_sort(lista):
    n=len(lista)
    comparaciones = 0
    intercambios = 0
    for i in range(n):
        minimo=i
        for j in range(i+1,n):
            comparaciones += 1
            if lista[j]< lista[minimo]:
                minimo=j
        if minimo != i:
            lista[i], lista[minimo] = lista[minimo], lista[i]
            intercambios += 1
    return lista, comparaciones, intercambios


def validarcero(numero):
    if numero <= 0:
        print("El número debe ser mayor que cero. Intente de nuevo.")





while True:
    print('Menu de Opciones:')
    print('1. Ingresar precios de productos')
    print('2. Metodos de ordenamiento')
    print('3. Vaciar lista de precios')
    print('4. Salir')
    opcion = int(input('Seleccione una opción: '))
    validarcero(opcion)
    if opcion == 1:
        longitud = int(input("Ingrese la cantidad de precios a ingresar (minimo 10): "))
        if longitud >= 10:
            break
        print("Debe ingresar al menos 10 precios.")
        for i in range(longitud):
            precio=int(input("Ingrese el precio del producto: "))


    elif opcion == 2:
        bubble = bubble_sort(precios.copy())
        print("Bubble Sort:", bubble[0])
        print("Comparaciones:", bubble[1])
        print("Intercambios:", bubble[2])
        insertion = insertion_sort(precios.copy())
        print("Insertion Sort:", insertion[0])
        print("Comparaciones:", insertion[1])
        print("Intercambios:", insertion[2])
        selection = selection_sort(precios.copy())
        print("Selection Sort:", selection[0])
        print("Comparaciones:", selection[1])
        print("Intercambios:", selection[2])
    elif opcion == 3:
        precios.clear()
        print("Lista de precios vaciada")
    elif opcion == 4:
        print("Gracias por usar el programa")
        break