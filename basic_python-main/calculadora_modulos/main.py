import os
import suma as s
import resta as r
from input import tomar_datos

os.system('clear')

while True:
    try:
        opcion = int(input('''\nElija una opción:

        1. Sumar
        2. Restar
        0. Salir

        > '''))
        if opcion == 1:
            x, y = tomar_datos()
            s.sumar(x, y)
        elif opcion == 2:
            x, y = tomar_datos()
            r.restar(x,y)
        elif opcion == 0:
            print('Terminado')
            break
    except ValueError: 
        print('\n¡¡¡ Error al ingresar la opción !!!')



