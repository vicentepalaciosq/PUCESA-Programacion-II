# Hecho por: Vicente Palacios
# Fecha: 30/05/25

# Por qué es necesario ordenar antes de realizar la búsqueda binaria?
# Es necesario ordenar porque la búsqueda binaria se basa en dividir la lista en mitades para saber en qué parte seguir buscando. 
# Si la lista no está ordenada, no se puede confiar en que el elemento esté en un lado o en otro 

# Qué pasaría si usamos búsqueda binaria sin ordenar primero?
# Si usamos búsqueda binaria sin ordenar primero, el algoritmo no funcionará correctamente y puede que no encuentre el elemento buscado,
# o que encuentre un elemento incorrecto

# Qué ventajas viste entre la búsqueda binaria y la búsqueda lineal?
# La principal ventaja de la búsqueda binaria es que es mucho más rápida, sobre todo si la lista es muy grande

# Cuál de los dos ordenamientos te pareció más intuitivo de implementar y por qué?
# A mí me pareció más fácil de entender el insertion sort, porque se parece a cómo uno ordena las cosas en la vida real

clientes=[
    ('Adrian', 100.0),
    ('Sebastian', 200.20),
    ('Mariana', 150.0),
    ('Lucia', 300.80),
    ('Carlos', 250.50),
    ('Ana', 400.70),
    ('Javier', 350.0),
    ('Laura', 500.39),
    ('Pedro', 600.40),
    ('Sofia', 450.60)
]

def insertion_sort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j][0].lower() > actual[0].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j][1] < lista[min_idx][1]: 
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def busqueda_lineal(lista, objetivo):
    contador = 0
    encontrado = False
    for i, cliente in enumerate(lista):
        contador += 1
        if cliente[0].lower() == objetivo.lower():
            encontrado = True
            print('Se hicieron', contador, 'comparaciones')
            return i, contador
    if not encontrado:
        print("\nCliente no encontrado.")
    return -1, contador

def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    contador=0

    while inicio <= fin:
        medio = (inicio + fin) // 2
        contador += 1
        nombre = lista[medio][0].lower()
        if nombre == objetivo.lower():
            encontrado=True
            print('Se hicieron', contador, 'comparaciones')
            return medio, contador
        elif objetivo.lower() < nombre:
            fin = medio - 1
        else:
            inicio = medio + 1
    return -1, contador

def validar(numero):
    if numero<=0 or numero>4:
        print('Escoga una opcion valida')

def separar():
    print('----------------------------------------------')

clientes_ordenados=insertion_sort(clientes.copy())

while True:
    separar()
    print('\n\t\tMenu de Opciones\n')
    separar()
    print('1. Agregar cliente')
    print('2. Buscar cliente')
    print('3. Ordenar clientes')
    print('4. Salir')
    separar()
    opcion = int(input('\nIngrese una opcion: '))
    if opcion == 1:
        nombre = input('Ingrese el nombre del cliente: ')
        saldo = float(input('Ingrese el saldo del cliente: '))
        clientes.append((nombre, saldo))
        separar()
        print(f'Cliente {nombre} agregado con saldo {saldo:.2f}.')
    elif opcion == 2:
        producto_a_buscar = input("\nIngrese el nombre del cliente a buscar: ")
        pos, comparaciones = busqueda_binaria(clientes_ordenados, producto_a_buscar)
        if pos != -1:
            print(f"Cliente encontrado: {clientes_ordenados[pos]} en posición {pos}")
        else:
            
            print("\nCliente no encontrado.")
    elif opcion == 3:
        clientes_ordenados_insertion=insertion_sort(clientes.copy())
        clientes_ordenados_selection=selection_sort(clientes.copy())
        separar()
        print("\nClientes ordenados por: \n")
        separar()
        print("Clientes por Nombre:")
        separar()  
        for cliente in clientes_ordenados_insertion:
            
            print(f"{cliente[0]}: {cliente[1]:.2f}")
        separar()
        print("Clientes por Saldo:")
        separar()
        for cliente in clientes_ordenados_selection:
            print(f"{cliente[0]}: {cliente[1]:.2f}")
        input("\nPresione enter para continuar...")
    elif opcion == 4:
        print('Gracias por usar el programa')
        break
    else:
        validar(opcion)
        separar()
        print('Opcion no valida, por favor intente de nuevo.')