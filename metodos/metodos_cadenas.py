cadena1 = "HolaNacho"
cadena2 = "123 quE hACes mirAndo mi githUb tAn A fondo?"
cadena3 = "1234"

#Los metodos van, dato.metodo()
#Si no pongo () falla y si es funcion(dato) no se concidera metodo

#Upper - todo a mayusculas
#Lower - todo a minusculas
#Capitalize - primera en mayuscula el resto a minuscula

mayus = cadena1.upper()
minus = cadena1.lower()
capital = cadena2.capitalize()

#Find - encuentra la primera aparición del valor espesificado, sino devuelve -1
#Index - encuentra la primera aparición del valor especificado, sino devuelve una excepción

find = cadena1.find("la N")
index = cadena2.index("1")

#Isnumeric - si es un numerico devuelve true
#Isalpha - si es alfanumerico devuelve true (solo valido de a-z y de A-Z, nada de espacios o caracteres especiales)

numeric = cadena3.isnumeric()
alpha = cadena1.isalpha()

#Count - devuelve cantidad de veces que ocurre una subcadena en otra
#Len - cuenta los caracteres de una cadena

count = cadena2.count("A")
len1 = cadena3.__len__()
len2 = len(cadena3)
#__len__ es un metodo que usa la funcino len() sobre si mismo
true = len1 == len2

#Endswith - verifica que termine con un caracter
#Startswith - verifica que arranque con un caracter

endswith = cadena3.endswith("34")
startswith = cadena1.startswith("Ho")

#Replace - remplaza un valor dentro de la cadena por otro
#Split - separa la cadena cada ves que encuentra el parametro ingresado y borra esa aparición del parametro

replace = cadena1.replace("Ho","OASODMASMDLMASLDMADLKASMDLKALKDM")
split = cadena2.split("A")

resultado = replace
resultado_split = split
print(resultado_split [1 + 2])
print(resultado)