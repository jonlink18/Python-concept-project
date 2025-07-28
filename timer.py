#Temporizador

import time

try:
    segundos = int(input("Cuantos segudos quieres: "))
    print (f"Iniciando temporizador de {segundos} segundos...")
except ValueError:
    print("Por favor, ingresa un numero valido")

while segundos > 0:
    print(segundos)
    time.sleep(1)
    segundos -=1

print("⏳ ¡Tiempo terminado!") 
