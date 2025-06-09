# Hecho por: Vicente Palacios
# Fecha: 09/06/2025


historial=[]
historial.append('www.google.com')
historial.append('www.python.org')
historial.append('www.stackoverflow.com')


while True:
    print('\n--------Menu de opciones---------\n')
    print('1. Revisar historial')
    print('2. Eliminar pagina actual')
    print('3. Visitar nueva pagina')
    print('4. Mostrar  pagina actual')
    print('5. Mostrar si el historial vacio')
    print('6. Salir')
    opcion=int(input('\nIngrese una opcion: '))
    if opcion==1:
        print('Historial: ',historial)
        input('Presione ENTER para continuar...')
    elif opcion==2:
        if len(historial)==0 :
            print('El historial esta vacio')
        else:
            pagina=historial.pop()               
            print('Volviendo atras desde: ',pagina)
            if len(historial)>0:
                print('Pagina actual: ',historial[-1])  
            else:
                print('Ya no hay paginas en el historial')          
        input('Presione ENTER para continuar...')
    elif opcion==3:
        nuevapag=input('Ingrese la nueva pagina: ')
        historial.append(nuevapag)
        print('Entrando a',nuevapag)
        input('Presione ENTER para continuar...')
    elif opcion==4:
        print('Pagina actual: ',historial[-1])
        input('Presione ENTER para continuar...')
    elif opcion==5:
        if len(historial)==0:
            print('El historial esta vacio')
        else:
            print('El historial no esta vacio')
        input('Presione ENTER para continuar...')
    elif opcion==6:
        print('Saliendo...')
        break
    elif opcion>6 or opcion<1:
        print('Ingrese una opcion valida')