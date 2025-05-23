#Matriz



matriz = [["Alfredo", "Jorge", "Donald"], ["David", "Montalvan", "Mishack"], ["Ashly", "Asael", "Loquendo"]]
print("-"*37)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>10}", end = " ")
    print("|")
    print("-"*37)
    