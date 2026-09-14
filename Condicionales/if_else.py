edad = 17

if edad >= 18:
    print ("mayor de edad")
    #esto es parte de condicional
#esto no
else:
    print ("menor de edad")
    #parte del condicional

#fuera de cualquier condicional (se ejecuta sin importar nada)
print ("Hola")

password = "1234"
password_tried = "1234"

if password == password_tried:
    print ("iniciando sesion")
    #esto es parte de condicional
#esto no
else:
    print ("Incorrecto")
    #parte del condicional

#fuera de cualquier condicional (se ejecuta sin importar nada)
print ("Hola")


#Elif e ifs anidados
presio = 10000
sueldo = 1000000
if presio >= 10000:
    if sueldo >= 1000000:
        print ("compral")
    else:
        print ("no compral")
elif presio >= 1000:
    print ("ta caro en Arg")
else:
    print ("ta varato")
    

