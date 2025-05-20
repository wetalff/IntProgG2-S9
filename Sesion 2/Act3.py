#Promedio de calificaciones
#✓ Solicita al usuario 8 calificaciones, guárdalas en una lista y calcula el
#promedio.

notas = []

for i in range(8):
    puntuacion = int(input(f"Ingrese la nota {i+1}: "))
    notas.append(puntuacion)

suma_total = sum(notas)
prom = suma_total / 8

print("El promedio de las 8 clases es de: ", prom)