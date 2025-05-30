#Listas=[]
#Diccionarios={}
# import array
#Array es una lista de elementos del mismo tipo, se declaran con el tipo de dato y el tamaño. 
#Remove. Elimina el primer elemento de la lista que coincide con el valor dado.
#Pop. Elimina el elemento en la posición dada y lo devuelve.


lista=[10,20,30,30,40,50,30,20]
lista.remove(30)
print(lista)
lista.pop(0) 
print(lista) 

#Recorrer una lista con un bucle for
numeros=[1,2,3,4,5,6,7,8,9,10]
for num in numeros:
    print(num)

suma=0
for num in numeros:
    suma+=num
print('Suma:',suma)


#Encontrar el mayor de una lista
mayor=numeros[0]
if num>=mayor:
    mayor=num
print('Mayor:',mayor)

#Cuantos numeros pares hay en la lista
pares=0
for num in numeros:
    if num%2==0:
        pares+=1
print('Pares:',pares)


#Generar una lista cin cuadrados de los numeros del 1 al 5
cuadrados=[]
for num in range(1,6):
    cuadrados.append(num**2)
print('Lista de cuadrados:',cuadrados)





