
#Crear lista (se puede modificar)
lista = ["Hola", "Mundo", True, 123]

#Crear tupla (no se puede modificar)
tupla = ("Hola", "Mundo", True, 123)

#Esto se puede
lista[1] = "Javier"

#Esto no se puede
#tupla[1] = "Javier"

print (lista)
print (lista [1])

print (tupla)
print (tupla [1])


#Crear conjunto (no se accede a elemntos por indice y no almacena datos duplicados)
conjunto = {"Hola" , "Chau", 123}

#se puede
print (conjunto)

#no se puede
#print (conjunto[3])

#Creando un diccinoario
diccionario = {
    'nombre' :  "Juan",
    'apellido' : "Perez",
    'numero_random' : 123,
    'es_real' : True
}

#La estructura es "Key : value" y separamos por comas y enters
#Diccionario {
# key1 : value1,
# key2 : value2,
# key3 : value3    
#}

#Se puede
diccionario['nombre'] = "Pedro"

#como printear
print (diccionario)
print (diccionario['nombre'])
print (diccionario['numero_random'] + 1)
#print (diccionario [key])
