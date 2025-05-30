lista=[6,20,17,1,8]
nueva_lista=[]
#Ordernar la lista de menor a mayor
for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        if lista[i]>lista[j]:
            lista[i],lista[j]=lista[j],lista[i]
print(lista)