diccionario = {
    "Nombre" : "Juan",
    "Apellido" : "Perez",
    "edad" : 18,
    "altura" : 1.84
}

#Keys - Devuelve las claves (sirve para iterar)

claves = diccionario.keys()

print (claves)

#Gey - Devuelve el dato con la key correcta (si hay )
#buscar = diccionario("Nombre") funciona pero no lanza excepcion si falla
buscar_valor_de_Nombre = diccionario.get("Nombre")

print (buscar_valor_de_Nombre)

#Pop - elimina un elemento del diccionario

diccionario.pop("Apellido")

print(diccionario)

#Items - obtengo un elemento dict_items iterable

diccionario_iterable = diccionario.items()

print(diccionario_iterable)


#Clear -  Elimina todo el diccionario

diccionario.clear()

print(diccionario)