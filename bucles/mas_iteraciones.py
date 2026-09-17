frutas = ["manzana", "banana", "pera", "ciruela", "naranja"]

for fruta in frutas:
    if fruta == "banana":
        print(f"No me gusta la {fruta}")
        continue #continue, termina esta iteración y pasa a la siguiente
    print(f"Que rica {fruta}")
    
for fruta in frutas:
    if fruta == "ciruela":
        print(f"Comer {fruta} hace que me duela la pansa, no quiero mas")
        break #Rompe el ciclo del for directamente
    print(f"Que rica {fruta}")
else:
    print ("Hola") #Al usar un else y un break, el else no se ejecuta
    
cadena = "Hola, como va?"

#recorrer cadena de texto
for letra in cadena:
    print ("letra")

numeros = [1,2,3,4,5]
#for en una sola linea de código
numeros_duplicados = [x * 2 for x in numeros]

print (numeros_duplicados)