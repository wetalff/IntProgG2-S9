#Arreglos de tipo entero

array_int = [5, 4, 3, 2, 1]
print("Array de enteros:", array_int)
#Ordenar el arreglo de menor a mayor
array_int.sort()
print("Array de enteros ordenados:", array_int)
#Ordenar de mayor a menor
array_int.sort(reverse=True)
print("Arrays de enteros ordenados de mayor a menor", array_int)
#Buscar un elemento en el arreglo
elemento =  4
if elemento in array_int:
    print(f"El elemento{elemento} se encuentra en el arreglo.")
else:
    print(f"El elemento {elemento} no se encuentra en el arreglo.")
    
#Insertar un elemneto en el arreglo