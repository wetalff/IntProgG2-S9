#Sumar elementos en posiciones pares
#✓ Suma los elementos que se encuentran en posiciones pares de la lista.

numeros = [4, 7, 10, 3, 8, 2, 5, 9, 1, 6]

suma_pares = 0

for i in (numeros):
    if i % 2 == 0:
        suma_pares += i

print("Lista de números:", numeros)
print("Suma de elementos en posiciones pares:", suma_pares)