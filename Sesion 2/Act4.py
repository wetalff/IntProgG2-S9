#Buscar un elemento
#✓ Dada una lista de palabras, solicita al usuario una palabra y muestra si está
#o no en la lista.

Lista = ["MOUSE", "TECLADO", "MONITOR", "PC", "AUDIFONOS"]
 
 
palabra = input("Ingrese la palabra para ver si esta en la lista: ").upper()

if palabra in Lista:
    print("La palabra SI esta en la lista")
else:
    print("La palabra NO esta en la lista")


