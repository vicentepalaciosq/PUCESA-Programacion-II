
tareas = []
tareas.append("Estudiar pilas en Python")  #push
tareas.append("Hacer ejercicios de estructuras de datos")  #push
tareas.append("Leer documentación oficial de Python")  #push


tareas1=[]
tareas1.append("Estudiar pilas en Python")  
tareas1.append("Hacer ejercicios de estructuras de datos")  
tareas1.append("Leer documentación oficial de Python")

while True:
    print('\n MENU DE OPCIONES \n')
    print('1. Ver todas las tareas')
    print('2. Ver la ultima tarea')
    print('3. Eliminar la ultima tarea')
    print('4. Verificar si hay tareas pendientes')
    print('5. Ver pila original y depues de modificarla')
    print('6. Salir')
    opcion=int(input('\nIngrese una opcion: '))
    if opcion == 1:
        print("Tareas pendientes:", tareas)
        input('Presione enter para continuar...')
    elif opcion==2:
        if tareas:
            print("Tarea más reciente:", tareas[-1]) #peek
        else:
            print("No hay tareas pendientes.")
        input('Presione enter para continuar...')
    elif opcion==3:
        if tareas:
            completada = tareas.pop() #pop
            print("Tarea completada:", completada)
        else:
            print("No hay tareas para completar.")
        input('Presione enter para continuar...')
    elif opcion==4:
        if len(tareas) == 0:  #isEmpty
            print("Todas las tareas han sido completadas.")
        else:
            print("Tareas restantes:", tareas)
        input('Presione enter para continuar...')
    elif opcion==5:
        print('Pila original: ', tareas1)
        print('Pila modificada: ', tareas)
        input('Presione enter para continuar...')
    else:
        print('Gracias por usar el programa')
        break



