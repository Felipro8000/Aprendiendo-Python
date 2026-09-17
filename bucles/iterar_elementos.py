animales = ["gato", "perro", "raton", "toro"]

#Recorriendo la lista animales
for animal in animales:
    print (f"Ahora la variable animal es {animal}")
    
numeros = [12, 24, 63, 62]

#Recorriendo la lista numeros y printeando su valor por 10
for numero in numeros:
    print (numero * 10)

#Como recorrer dos listas al mismo tiempo? (sirve para mas de 2, se puede con 3, 4 ,5...)
for numero,animal in zip(numeros, animales):
    print (f"numero = {numero}")
    print (f"animal = {animal}")
#LAS LISTAS TIENEN QUE TENER LA MISMA CANTIDAD DE ELEMENTOS     


#Usando for con range()
for num in range (5,10): #si le pongo solo un numero va de 0 a ese numero
    print (num)
    
    
#Forma NO optima de recorrer lista
for num in range(numeros.__len__()):
    print (numeros[num])
#NO FUNCIONA PARA CONJUNTOS


#Forma correcta de recorrer una lista
for num in enumerate(animales):
    print(f"enumerate devuelve {num}")
    print(f"el indice es {num[0]}")
    print(f"el animal es {num[1]}")
    
#Forma correcta y elegante
for i,animal in enumerate(animales):
    print(f"el indice es {i}")
    print(f"el animal es {animal}")
    
#Como usar else en for, el else se va a ejecutar SIEMPRE despues de que termine el for (a menos que haya un break)
for num in numeros:
    print(numero)
else:
    print("La lista numeros termino")

#Todo lo anterior funciona exactamente igual para tuplas y conjuntos (conjuntos casi)