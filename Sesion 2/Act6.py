#Invertir una lista
#✓ Pide 10 números al usuario, guárdalos en una lista e imprímelos en orden
#inverso.

Numeros = []
for i in range(10):
 Num = int(input("Ingrese un numero a la lista: "))
 Numeros.append(Num)
 
 
print("Los numeros ingresados a la lista en orden inverso es: ")
print(Numeros[::-1])
