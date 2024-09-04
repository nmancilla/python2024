from tiempo import calculo_tiempo
import time

def ordenar(pizza_base):
    tiempo = calculo_tiempo(pizza_base)
    print(f'Su Pizza estará lista en {tiempo} minutos')
    ordenar = input('Desea ordenar ahora? S/N: ').upper()
    if ordenar == 'S':
        print('Gracias por ordenar en Pizza Jat')
        print('Disfrute su pizza')
        exit(time.sleep(1))