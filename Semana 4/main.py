from funciones import registrar_paciente, registrar_consulta,buscar_paciente, mostrar_datos, mostrar_todo

def menu():
    while True:
        print('\nGestion de Consultas Medicas\n')
        print('1. Regristrar un nuevo paciente ')
        print('2. Registrar una consulta medica a un paciente existente')
        print('3. Mostrar los datos completos de un paciente ')
        print('4. Mostrar pacaientes registrados')
        print('5. Salir')
        opcion = int(input('Ingrese la opcion que desee: '))
        if opcion>5 or opcion<1:
            print('Error. Seleccione una opcion valida')
        else: 
        
            if opcion==1:
                registrar_paciente()
            elif opcion==2:
                registrar_consulta()
            elif opcion==3:
                mostrar_datos()
            elif opcion==4:
                mostrar_todo()
            elif opcion==5:
                print('Gracias por usar el programa')
                break


            
menu()