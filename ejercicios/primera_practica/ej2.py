#a) pedir al ususario una frase y calcular cuanto se tardaría en decir
#b) si el usuario se pasa del minuto, decir que es mucho texto
#c) yo hablo 30% mas rapido del promedio, cuanto tardo en decirlo?
# Cada segundo puedo decir dos palabras

frase = input("Deci la frase: \n")
palabras = frase.split(" ")

segundos = float (palabras.__len__()) / 2

if (segundos < 60):
    print (f"Decir eso se tardaría: {segundos} segundos")
    print (f"Yo puedo decirlo en: {segundos - (segundos * 0.3):.2f} porque soy mas rapido")
elif (segundos < 90):
    print ("Te tardas mucho tiempo")
    print (f"Yo puedo decirlo en: {segundos - (segundos * 0.3):.2f} porque soy mas rapido") 
else:
    print ("Te tardas mucho tiempo, es muy larga la frase")
