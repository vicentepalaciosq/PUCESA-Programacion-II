from funciones import registrar_libro, buscar_libro, registrar_prestamo, mostrar_datos,  mostrar_todoslibros
def menu():
    while True:
        print('\n MENU DE OPCIONES \n')
        print('1. Registrar un nuevo libro')
        print('2. Registrar un prestamo')
        print('3. Mostrar informacion de un libro')
        print('4. Mostrar todos los libros')
        print('5. Salir')
        opcion=int(input('Ingrese una opcion: '))
        if opcion>5 or opcion<1:
            print('Escoja una opcion valida')
        elif opcion == 1:
            registrar_libro()
        elif opcion == 2:
            registrar_prestamo()
        elif opcion == 3:
            mostrar_datos()
        elif opcion == 4:
            mostrar_todoslibros()
        elif opcion == 5:
            print('Gracias por usar el programa!')
            break


menu()