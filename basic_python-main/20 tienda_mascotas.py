'''
Voy a realizar un ciclo infinito
En cada iteración pregunto lo siguiente:
    - nombre de la especie
    - precio de la unidad
    - cantidad de ejemplares

Si el usuario ingresa como nombre de la especie un "0", entonces termina el ciclo.
Imprimo la lista de todas las especies

BONUS: Una vez finalizado, imprimir el total del dinero en especies
'''

# mascotas = []
# while True:
#     especie = input('\nIngrese nombre de la especie (0 para salir): ')
#     if especie == '0':
#         break
#     precio = int(input('Ingrese precio de la unidad: '))
#     cantidad = int(input('Ingrese cantidad: '))

#     animales = {
#         'especie': especie,
#         'precio': precio,
#         'cantidad': cantidad
#     }
#     mascotas.append(animales)

# suma = 0
# for mascota in mascotas:
#     precio_total = mascota['precio'] * mascota['cantidad']
#     print(f"El precio total de {mascota['especie']} es de ${precio_total}")










# print('\nBienvenido al ADMIN de la tienda de mascotas')
# def tiendas():
#     mascotas = []
#     while True:
#         # Pedidmos datos
#         especie = input('\nIngrese la nueva especie: ')
#         if especie == '0':
#             break
#         precio = int(input('Ingrese el precio por ejemplar: '))
#         cantidad = int(input('Ingrese el número de ejemplares: '))
#         # Armamos diccionarios
#         nueva_mascota = {
#             'especie': especie,
#             'precio': precio,
#             'cantidad': cantidad
#         }
#         # Agregamos el diccionario a la lista de mascota
#         mascotas.append(nueva_mascota)
#         # Calcular el total de total del inventario
#         total = 0
#         for mascota in mascotas:
#             total += mascota['precio'] * mascota['cantidad']
#     #Imprimir los totales
#     print(f'En la tienda hay ${total} en especies')
#     print(mascotas)
# tiendas()
