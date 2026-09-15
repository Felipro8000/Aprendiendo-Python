lista1 = [1, 2, 33, 42, True, False, 5, 6]
lista2 = [1, "asd", "jkasjaj", "Hola"]
lista3 = []

#Len - cuenta cantidad de elementos de la lista

len1 = lista1.__len__
len2 = len(lista1)

#Append - añade una elem al final de la lista

lista3.append("Holas")

#Insert - ñaade un elemento a la lista en el indice indicado

lista3.insert(2 , "Holas")

#Extend - extiende la lista con otra lista

lista3.extend(lista2)

#Pop - elimina el elemento de la lista en el indice indicado (usando negativos da la vuelta por el final)

lista2.pop(2)

#Remove - elimina un elemento de la lista por su valor (si no existe tira error)

lista1.remove(1)

#Clear - elimina todos los elementos de la lista

lista2.clear()

#Sort - ordena la lista de menor a mayor (no soporta STRs)

lista1.sort()
print(lista1)

lista1.sort(reverse=True) #da vuelta la lista
print(lista1)

#Reverse - invierte los elementos de una lista

print(lista3)

lista3.reverse()
print(lista3)

#Index - busca el elemento en una lista, si busco "Hol" y tengo el elemento "Hola" no funciona porque busca 100% de igualdad
index = lista1.index(1)

resultado = index

print (resultado)
