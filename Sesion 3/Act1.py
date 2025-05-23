# Registro de calificaciones
#Un docente desea registrar las calificaciones de sus 10 estudiantes en un examen.
#El programa debe:
#• Solicitar las calificaciones (sólo se permiten entre 0 a 100).
#• Mostrar el promedio, la calificación más alta, la más baja y cuántos aprobaron (>=
#70).

Calificaciones = []
Suma = 0

for i in range(10):
    Nota = float(input(f"Ingrese la nota del estudiante {i+1}: "))
    Calificaciones.append(Nota)
    Suma += Nota
    if Nota >= 70:
        print("El estudiante aprobo 👍")
    
Mayor = max(Calificaciones)
Menor = min(Calificaciones)

Prom = Suma / 10
print("El promedio de las notas de los 10 estudiantes es de: ", Prom)
print("La calificacion mas alta fue de: ", Mayor)
print("La calificacion mas baja fue de: ", Menor)

    