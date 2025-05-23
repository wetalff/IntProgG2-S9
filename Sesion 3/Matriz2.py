#Matriz 2

matriz = [[1.73, 2.294], [3.8165748930, 4.45]]
print("-"*17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:> 5}", end = " ")
    print("|")
    print("-"*17)
    