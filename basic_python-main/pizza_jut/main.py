import os
import sys
import time
import datos as d
from masa import cambiar_tipo_masa
from salsa import agregar_salsa
from add import agregar_ingredientes
from remove import quitar_ingredientes
from show import mostrar_ingredientes
from ordenar import ordenar

pizza_base = d.ingredientes
clear = 'cls' if sys.platform == 'win32' else 'clear'


def menu():
    os.system(clear)
    print('\n                *** Bienvenido a Pizza Jut ***')
    while True:
        try:
            time.sleep(0.5)
            opcion = int(input(d.principal))
            if opcion == 1:
                os.system(clear)
                eleccion = input(d.tipo_de_masa)
                cambiar_tipo_masa(pizza_base, eleccion)
            elif opcion == 2:
                os.system(clear)
                eleccion = input(d.salsa)
                agregar_salsa(pizza_base, eleccion)
            elif opcion == 3:
                os.system(clear)
                eleccion = int(input(d.ingredientes_disponibles))
                agregar_ingredientes(pizza_base, eleccion)
            elif opcion == 4:
                os.system(clear)
                quitar_ingredientes(pizza_base)
            elif opcion == 5:
                os.system(clear)
                ordenar(pizza_base)
            elif opcion == 6:
                os.system(clear)
                mostrar_ingredientes(pizza_base)
            elif opcion == 0:
                os.system(clear)
                print('Su pedido ha sido cancelado. Gracias por contactarse a Pizza JAT')
                exit(time.sleep(1))
        except ValueError:
            print('     **** Opción no valida ****')

if __name__ == '__main__':  
    menu()