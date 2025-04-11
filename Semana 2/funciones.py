'''

def funcion(nombre):
    print('Estamos estudiando Python', nombre)
funcion('Vicente')
print('\n')

def datos(nombre, apellido):
    print('Estamos estudiando Python', nombre, apellido)
datos('Vicente','Palacios')

def area_triangulo(base,altura):
    calc=base*altura/2
    print(calc)
area_triangulo(2,3)
area_triangulo(4,5)
print('\n')


def welcome(nombre='Jairo',lenguaje='Python'):
    print('Bienvenido a', lenguaje, nombre+'!')
welcome('Vicente')
welcome('Vicente','PHP')
welcome()

def menu(*platos):
    print('Hoy tenemos: ', end='')
    for plato in platos:
        print(plato, end=', ')
menu('pasta','pizza','ensalada')


for j in range(0,5+1):
    print('Tabla del ',j)
    for k in range(0,5+1):
        for l in range(0,5+1):
            print(j,'*',k,'*',l,'=',j*k*l)

for r in [10,200,38]:
    print('Su cuadrado es: ', r**2)


for t in [1,2,3]:
    print('Tabla del',t)
    for q in [0,1,2,3]:
        print(t,'*',q,'=',t*q)


'''



#for i in range(0,10+1):
#    if i%2==0:
#        print('El numero',i,'es par')
#    else: 
#        print('El numero',i,'es impar')

#for i in range(0,10+1):
#    if i%2==0:
#        print('El numero',i,'es par')

#for j in range(0,10+1):
#    if j%2!=0:
#        print('El numero',j,'es impar')


#Funciones recursivas

#def cuenta_regresiva(numero):
#    numero-=1
#    if numero > 0:
#        print(numero)
#        cuenta_regresiva(numero)
#    else:
#        print('Booooooooom!')
    #print('Fin de la funcion', numero)
#cuenta_regresiva(5)

class persona:
    def __init__(self,nombre,edad,ocupacion):
        self.nombre=nombre
        self.edad=edad
        self.ocupacion=ocupacion
    def descripcion(self):
        return f'Nombre: {self.nombre},Edad:{self.edad},Ocupacion:{self.ocupacion}'

def mostrarmenu():
    print('\n---Gestion de personas---')
    print("1. Agregar personas")
    print('3. Mostrar todas las personas')
    print('3. Buscar por nombre')
    print('4. Salir')


personas=[]

while True:
    mostrarmenu()
    opcion=int(input('Seleccione una opcion: '))
    if opcion ==1:
        nombre=input('Ingrese el nombre: ')
        edad=int(input('Ingrese la edad de la persona: '))
        ocupacion=input('Ingrese la ocupacion de la persona: ')
        nueva_persona=persona(nombre,edad,ocupacion)
        personas.append(nueva_persona)
        print(f"La persona {nombre} ha sido agregada")
    elif opcion == 2:
        if len(personas)>0:
            print('\n---Lista de personas---')
            for persona in personas:
                print(persona.descripcion())
        else:
            print('No hay personas en la lista')
    elif opcion==3:
        if len(personas)>0:
            nombre_buscar=input('Ingrese el nombre de la persona a bsucar: ')
            encontrada=False
            for persona in personas:
                if persona.nombre.lower()==nombre_buscar.lower():
                    print('Persona encontrada: ')
                    print(persona.descripcion())
                    encontrada=True
                    break
            if not encontrada:
                print(f"No se encontro a {nombre_buscar} en la lista.")
        else:
            print('No hay personas en la lista')
    elif opcion==4:
        print('Hasta luego!')
        break
    else:
        print('Opcion no valida')



