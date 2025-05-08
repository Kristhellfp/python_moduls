from programas.sumas import sumar2 
from programas.restas import restar2
from vistas.menu import cargar_menu
from vistas.lineas import cargar_lineas

from datetime import datetime
import threading
import os
import time

def mostrar_hora():
    while True:
        os.system("clear")
        print("Hora actual:", datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)

hilo_reloj = threading.Thread(target=mostrar_hora, daemon=True)
hilo_reloj.start()

programa = True
os.system("ls")

while programa:
    cargar_lineas(10)
    cargar_menu()

    try:
        respuesta = int(input("|[?]"))  
    except ValueError:
        print("Opción no válida")
        time.sleep(1)
        continue

    if respuesta == 1:  
        print("Sumar dos números")
        sumar2()
        time.sleep(2)

    elif respuesta == 2: 
        print("Restar dos números")
        restar2()
        time.sleep(2)
    
    elif respuesta == 0:
        print("|[::Fin del programa]")
        programa = False  
        time.sleep(1)
