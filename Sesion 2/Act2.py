#Sumar los elementos de una lista
#✓ Solicita 10 números al usuario, guárdalos en una lista y muestra la suma
#total.

numeros = []

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

suma_total = sum(numeros)

print("La suma de los números que ingresaste para la lista es:", suma_total)