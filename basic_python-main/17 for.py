# # Itera sitring
# for letra in 'hola como estas':
#     print(letra)






# # Imprime QUINA en los multiplo de 5
# for i in range(30): #(0,30,1)
#     print('Quina') if i % 5 == 0 else print(i)






# # Numero pares del 1 al 50
# for n in range(0, 50, 5): # Comienza en cero, hasta el 50, de 5 en 5
#     print(n)





# # Interando string y mostrando la posición usanodo enumerate
# texto = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme.'
# for num, letra in enumerate(texto):
#     print(f'El caracter {letra} está en la posición {num}')






# #Romper comtraseña ingresando por terminal: python 17\ for.py palabra
# import sys
# from string import ascii_lowercase

# def fuerza_bruta ():
#     clave = (sys.argv[1]).lower()
#     intentos = 0
#     for letra in clave:
#         for caracter in ascii_lowercase:
#             intentos += 1
#             if letra == caracter:
#                 break
#     print(f'Se logró romper la contraseñanen {intentos} intentos')
# fuerza_bruta()






# #Tablas de multiplicar
# for numero1 in range(1, 10):
#     print('\n')
#     print(f'Tabla del {numero1}:')
#     for numero2 in range(10):
#         print(f'{numero1} x {numero2} = {numero1 * numero2}')
