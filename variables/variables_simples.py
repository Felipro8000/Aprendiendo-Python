a = 2
b = 3
c = a + b
c += a
c -= b
print (c)
#definir variable con camelCase
nombreCompleto = "lucas"
#definir variable con snake_case (recomendación oficial de python)
nombre_completo = "dalto"
nombre = "Pedro"
bienvenida = "Hola " + nombre + " 123" #concatenar con +
#bienvenida = "Hola {nombre} {c}" así no
#bienvenida = f"Hola {nombre} {c}" así si
bienvenida = f"Hola {nombre} {c}" # Concatenar con f-strings

del c #borra c delete si pongo del antes de bienvenida tira error
print (bienvenida)

#operadores de pertenencia (in / not in)

print ("ola" in bienvenida) #se fija si hay un ola en bienvenida
print ("Pedro" in bienvenida) #se fija si hay un Pedro en bienvenida
print ("Juan" not in bienvenida) #se fija no si hay un Juan en bienvenida