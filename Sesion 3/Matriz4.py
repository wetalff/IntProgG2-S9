
Matriz = [[50, 50],
          [75, 10]]
print("-"*15)
for fila in Matriz:
    for columna in fila:
        print(f"|{columna:>5}", end = " ")
    print("|")
    print("-"*15)
    
for fila in Matriz:
    for columna in fila:
        print(f"|{columna * 1.15:.1f}", end = " ")
    print("|")
    print("-"*13)
    
          