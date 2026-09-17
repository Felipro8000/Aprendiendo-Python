diccionario = {
    "nombre" : "Juan",
    "apellido" : "Perez",
    "edad" : 64,
}


#recorriendo el diccionario y sacando solo las claves
for key in diccionario:
    print (key)

#recorriendo el diccionario y sacando las llaves y los datos
for key,dato in diccionario.items():#.items() me devuelve una lista de tuplas con la siguiente forma (Key,Dato)
    print(f"La key es: {key} y el dato es {dato}")