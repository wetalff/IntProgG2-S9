#Separar pares e impares
#✓ Llena una lista con 10 números enteros aleatorios entre 1 y 100, y
#sepáralos en dos listas: pares e impares.

import random

numeros = []
pares = []
impares = []

# Generar 10 números aleatorios entre 1 y 100
for _ in range(10):
    num = random.randint(1, 100)
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar resultados
print("Lista original:", numeros)
print("Números pares:", pares)
print("Números impares:", impares)