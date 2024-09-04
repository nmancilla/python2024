# # Transformar integer o float a string
# inte = int(input('Ingrese un número (integer): \n '))
# floa = float(input('Ingrese un número (float): \n '))
# print ('Nunmero integer: ' + str(inte))
# print ('Nunmero float: ' + str(floa))









#Operadores de asignación
#   a = 2 a toma el valor 2.
#   a += 2 a es incrementado en dos y asignado el valor resultante.
#   a -= 2 a es reducido en dos y asignado el valor resultante.
#   a *= 3 a es multiplicado por tres y asignado el valor resultante.
#   a /= 3 a es dividido por tres y asignado el valor resultante







#Contador:
# cont = cont + 1
# cont += 1

#Acumulador:
# acu = acu + valor
# acu += valor








# #Métodos disponibles para cada tipo de dato o escructura
# metodos = dir(list)
# for metodo in metodos:
#     print(metodo)








# # Pausas
# import time

# print('Comienza...')
# time.sleep(3)
# print('Han pasado 3 segundos')









# #Limpiar pantalla
# import os
# import sys

# clear = 'cls' if sys.platform == 'win32' else 'clear' # detecta el OS
# # ejecuta la limpieza
# os.system(clear)







# # Ingresar datos junto al nombre archivo con import sys
# # python 00\ apuntes_varios.py texto
# import sys
# palabra = (sys.argv[1]).lower()
# print(f'La palabra ingresada fue: {palabra}')