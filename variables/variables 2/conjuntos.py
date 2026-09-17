#Crear conjunto con set()

conjunto = set(("Dato 1", "Dato 2"))
print (conjunto)
conjunto = set(["Dato 1", "Dato 2"])
print (conjunto)

#Cosas que no puedo hacer
#conjunto = set (["Dato 1", ["Dato en lista 1", "Dato en lista 2"] ]) no se puede meter una lista dentro de un conjunto
#conjunto = set (["Dato 1", {"Dato en lista 1", "Dato en lista 2"} ]) no se puede meter un diccionario dentro de un conjunto

#Como meter conjunto dentro de otro?
#conjunto1 = {1, 2, 3}
#conjunto2 = {conjunto1 , 4}
#así no

conjunto1 = frozenset({1, 2, 3})
conjunto2 = {conjunto1, 4}
#Así si

print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1, 2, 3, 4}
conjunto2 = {1, 2, 4}

#en ves de issubset se puede usar tambien "conjunto2 <= conjunto1" es lo mismo
resultado = conjunto2 <= conjunto1
resultado2 = conjunto1.issubset(conjunto2)

print (f"2 subconjunto de 1?:{resultado}, 1 subconjunto de 2?: {resultado2}")

#en ves de issuperset se puede usar tambien "conjunto2 > conjunto1" es lo mismo
resultado = conjunto2 > conjunto1
resultado2 = conjunto1.issuperset(conjunto2)

print (f"2 superconjunto de 1?:{resultado}, 1 superconjunto de 2?: {resultado2}")

#Ver si dos conjuntos comparten elemento

resultado = conjunto1.isdisjoint(conjunto2)

if (resultado):
    print ("No tienen elementos en comun")
else:
    print("Tienen al menos 1 elemento en comun")

conjunto2 = {5, 6, 7}

resultado = conjunto1.isdisjoint(conjunto2)

if (resultado):
    print ("No tienen elementos en comun")
else:
    print("Tienen al menos 1 elemento en comun")
