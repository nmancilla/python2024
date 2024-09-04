# Librería para leer argumentos del programa
import sys
# Librería para esperar un segundo
import time

def main():
    # argumentos = sys.argv 
    # segundos = argumentos[1] #Solicita el argumento de la posición 1 (los segundos)
    segundos = int(sys.argv[1])

    while segundos > 0:
        print(segundos)
        time.sleep(0.4)
        segundos -= 1
    print('Boom!!')

main()