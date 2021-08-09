import time
import os

minutos = 0
numero = 0
segundos = 0

while numero >= 0:
    print("CRONÔMETRO")
    if segundos == 60:
        minutos = minutos + 1
        segundos = 0
    if minutos == 60:
        numero = numero + 1
        minutos = 0
    print(numero,':',minutos,':',segundos)   
    segundos = segundos + 1
    time.sleep(1)
    os.system("cls")
