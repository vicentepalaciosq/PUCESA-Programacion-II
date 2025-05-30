# numero=[1,20,3,4,5,20,6,7,8,20,9,10]
# nueva_lista=[]
# for i in numero:
#     if i!=20:
#         nueva_lista.append(i)
# print(nueva_lista)


# for num in numero:
#     if num==20:
#         numero.remove(num)
# print(numero)

# #Try except


# try:
#     num1=int(input('Introduce un numero: '))
#     print(num1)
#     num2=int(input('Introduce otro numero: '))
#     print(num2)
# except ValueError:
#     print('Error: No es un numero')
    


def busqued_lineal(lista,objetivo):
    for i in range(len(lista)):
        if lista[i]==objetivo:
            return i
    return -1
datos=[1,2,3,4,5,6,7,8,9,10]
print(busqued_lineal(datos,5)) 