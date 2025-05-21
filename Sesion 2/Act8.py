#Eliminar duplicados
#✓ Dada una lista con valores repetidos, crea una nueva lista sin duplicados.


Numeros = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
Numeros_no_dup = []
for elemento in Numeros:
    if elemento not in Numeros_no_dup:
        Numeros_no_dup.append(elemento)
print("Lista original:", Numeros)
print("Lista sin duplicados:", Numeros_no_dup)