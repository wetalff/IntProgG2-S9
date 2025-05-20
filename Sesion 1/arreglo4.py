import os
import random
import time


participantes = list()

while True:
    os.system("cls||clear")
    
    Nombre: str = input("Ingrese el nombre del participante (o 'fin' para terminar): ")
    if Nombre.lower() == "fin":
        break
    
    participantes.append(Nombre.upper())
 
 
os.system("cls||clear") 
print("Participantes agregados:", participantes)
for cont in range(10, 0, -1):
    os.system("cls||clear")
    print(cont)
    time.sleep(1)
    

ganador = random.randint(0, len(participantes) - 1)
print("El ganador es:", participantes[ganador])

   
    