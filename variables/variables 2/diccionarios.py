#Crear diccionario con dict()
diccionario = dict(nombre = "Juan", apellido = "Perez")

print (diccionario)

#Las listas y los conjuntos no pueden ser claves, las tuplas y los frozenset si pueden
#Esto no se puede:
#diccionario = {["Hola","Chau"] : "Juan", {1, 2} : "Perez"}

#Esto si se puede
diccionario = {("Hola", "Chau") : "Juan", frozenset([1, 2]) : "Perez"}

print (diccionario)

#Creando diccionario con fromkeys(), valor por defecto: None
#Tengo que poner dict.fromkeys porque es un metodo de el tipo dict
diccionario = dict.fromkeys(["Nombre", "Apellido", "Edad"])
print (diccionario)

diccionario = dict.fromkeys("12345") # "12345" = ['1','2','3','4','5']
print (diccionario)

diccionario = dict.fromkeys(["Nombre", "Apellido", "Edad"], "no se") #Cambio el valor por defecto none a "no se"
print (diccionario)