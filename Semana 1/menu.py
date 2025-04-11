print('Menu de opciones')
print('1. Suma')
print('2. Resta')
print('3. Multiplicacion')
print('4. Division')
opcion=int(input('Ingrese un numero del 1 al 4: '))
if opcion>4 or opcion<=0:
    print('Error, seleccione una opcion valida')
    opcion=int(input('Ingrese un numero del 1 al 4: '))
if opcion ==1:
    num1=float(input('Ingrese el primer numero: '))
    num2=float(input('Ingrese el segundo numero: '))
    sum=num1+num2
    print('El resultado de la suma es: ',sum)
elif opcion==2:
    num1=float(input('Ingrese el primer numero: '))
    num2=float(input('Ingrese el segundo numero: '))
    resta=num1-num2
    print('El resultado de la resta es: ',resta)
elif opcion==3:
    num1=float(input('Ingrese el primer numero: '))
    num2=float(input('Ingrese el segundo numero: '))
    mult=num1*num2
    print('El resultado de la multiplicacion es: ',mult)
elif opcion ==4:
    num1=float(input('Ingrese el primer numero: '))
    num2=float(input('Ingrese el segundo numero: '))
    if num2==0:
        print('Error, escriba un numero mayor que cero')
        num2=float(input('Ingrese el segundo numero: '))
    divi=num1/num2
    print('El resultado de la division es: ',divi)    









