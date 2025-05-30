#Realizado por: Vicente Palacios

#Que es busqueda lineal?
#Es una forma de buscar un elemento en una lista, revisando cada elemento uno por uno hasta encontrar el que buscamos
#Que es busqueda binaria?
#Es una forma de buscar un elemento en una lista, pero la lista tiene que estar ordenada. La busqueda binaria divide la lista en dos partes y busca en la parte donde puede estar el elemento, repitiendo el proceso hasta encontrarlo
#En que casos se usa cada una?
#La busqueda lineal se usa cuando la lista no esta ordenada o es muy pequeña. La busqueda binaria se usa cuando la lista esta ordenada y es grande

# Ejercicio en Clase: "Sistema de Búsqueda de Productos para una Tienda Virtual"

productos =sorted([
    "Laptop", "Celular", "Tablet", "Monitor", "Teclado", "Mouse", "Audifonos", "Cargador", "Parlante", "Impresora",
    "Escritorio", "Silla", "Disco Solido", "Proyector", "USB", "Disco Duro", "Router", "Smart TV", "Consola"
    , "Camara"
])

resumen=[]



print('\tMenu de Opciones\n')
print('\n1. Buscar un producto')
print('2. Resumen')
print('3. Salir\n')


while True:
    opcion=int(input('Ingrese una opcion: '))
    if opcion==1:
        #BSUQYEDA LINEAL
        buslienal=0
        encontrado=False
        productobuscar = input("Ingrese el nombre del producto que desea buscar: ")
        print('Busqueda Lineal')
        for producto in productos:
            buslienal+=1
            if producto.lower()== productobuscar.lower():
                print("El producto", productobuscar, "se encuentra en la lista")
                print('Se hicieron', buslienal, 'comparaciones')
                encontrado=True
                resumen.append(productobuscar)
                break              
        if not encontrado:
            print("El producto", productobuscar, "no se encuentra en la lista o no se ha rellenado correctamente")
            print('Se hicieron', buslienal, 'comparaciones')   
        
        #BUSQUEDA BINARIA
        inicio = 0
        fin = len(productos) - 1
        contador=0
        encontrado=False
        print('Busqueda Binaria')
        while inicio <= fin:
            medio = (inicio + fin) // 2
            contador += 1
            if productos[medio].lower() == productobuscar.lower():
                print("El producto", productobuscar, "se encuentra en la lista")
                print('Se hicieron', contador, 'comparaciones')
                encontrado=True
                break
            
            elif productos[medio].lower() < productobuscar.lower():
                inicio = medio + 1

            else:
                productos[medio].lower() > productobuscar.lower()
                fin = medio - 1

        if not encontrado:
            print("El producto", productobuscar, "no se encuentra en la lista o no se ha rellenado correctamente")
            print('Se hicieron', contador, 'comparaciones')   
    elif opcion==2:
        print('Resumen')
        print('Los productos que se han buscado son:')
        for producto in resumen:
            print(producto)
        
    elif opcion==3:
        
        print('Gracias por usar el programa')
        break





