#Contar elementos mayores que un número
#Dada una lista de 10 números, contar cuántos son mayores que 50.


numeros = [10, 50, 30, 100, 456, 37485, 56, 2, 9, 500]

contador = 0
for num in numeros:
    if num > 50:
        contador += 1

print(f"Hay {contador} número(s) mayores que 50.")