#Generando datos
datos_tupla = ("Juan", "Perez",31)
datos_lista = ["Juan", "Perez",31]

#Desempaquetando datos
nombre, apellido, años = datos_tupla
nombre2, apellido2, años2 = datos_lista

print(años)
print(años2)

#Ahora con conjuntos
mi_conjunto = {'azul', 'verde', 'rojo', 123}

# Desempaquetado directo
color1, color2, color3, numero = mi_conjunto

print(color1)
print(color2)
print(color3)
print(numero)

#Como los conjuntos no tienen orden, no se asigna correctamente
#Skibidi toilechi