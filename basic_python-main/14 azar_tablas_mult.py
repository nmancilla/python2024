# import random
# def main():
#     ganador = random.randint(1, 10)
#     print(f'Numero secreto -> {ganador}')
#     while True:
#         opcion = int(input('Adivine un numero del 1 al 10: '))
#         if opcion == ganador:
#             print('Felicidades, ganaste!')
#             break
#         else:
#             print('Perdiste, pero aprendiste!')
# main()






# Tablas de multiplicar
# def tablas():
#     i = 1
#     while i <= 10:
#         print('\nLa tabla del ' + str(i))
#         j = 1
#         while j <= 10:
#             frase = str(i) + ' x ' + str(j) + ' = ' + str(i*j)
#             print(frase)
#             j += 1
#         i += 1
# tablas()
# # Para impimir en un documento de texto: python azar_tablas.py > tabla.txt