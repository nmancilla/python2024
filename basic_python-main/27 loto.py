# Crear un programa que permita simular un sorteo del Loto.
# Reglas: Se tiene un pool de números del 1 al 41, y uno a uno se tomarán 6 números al azar, 
# y un séptimo que representará el comodín

import random

pool = [n for n in range(1,42)]

posiciones = [
    'primer número', 
    'segundo número', 
    'tercer número', 
    'cuarto número', 
    'quinto número', 
    'sexto número', 
    'comodín'
]

def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f'El {posicion} es {elegido}')

for posicion in posiciones:
    sacar_numero(posicion)
    # Opcional
    print(pool) # número ha sido eliminado

print("Sorteo ha finalizado")