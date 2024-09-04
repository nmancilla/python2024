# # Iterando una lista
# ciudades = ['Puerto Montt', 'Talaca', 'Valdivia', 'Santiago', 'Viña del Mar']
# for ciudad in ciudades:
#     print(f'Este año visitaré: {ciudad}')






# # Iterando tomando el índice usando enumerate
# ciudades = ['Puerto Montt', 'Talaca', 'Valdivia', 'Santiago', 'Viña del Mar', 'Villa Alemana', 'Quilpué']
# for indice, ciudad in enumerate(ciudades): #permite tomar el indice y nombre
#     frase = f'La ciudad {ciudad} está en la posición {indice}'
#     print(frase)









# # Método zip para unir listas
# prefijo = ['La','El','La','El']
# frutas = ['manzana', 'platano','frutilla','tomate']
# colores = ['verde','amarillo','roja','rojo']
# for p, fruta, color in zip(prefijo, frutas, colores):
#     print(f'{p} {fruta} es de color {color}')






# # Buscando una palabra en una lista usando in e enumerate
# palabra = None
# while palabra != 'x':
#     palabra = input('Ingrese palabra a buscar o ingrese x para salir: ')
#     cuentos = ['En', 'un', 'lugar', 'de', 'la', 'Mancha,', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme,', 'no', 'ha', 'mucho', 'tiempo', 'que', 'vivía', 'un', 'hidalgo', 'de', 'los', 'de', 'lanza', 'en', 'astillero,', 'adarga', 'antigua,', 'rocín', 'flaco', 'y', 'galgo', 'corredor.']
#     encotrado = False
#     for indice, cuento in enumerate(cuentos):
#         if palabra == cuento:
#             encotrado = True
#             print(f'La palabra {cuento} está en la posición {indice}')
#     if encotrado == False:
#         print('La palabra no se encontró')





# # Buscando una palabra en una lista usando in e enumerate (otra forma)
# palabra = None
# while palabra != 'x':
#     palabra = input('Ingrese palabra a buscar o ingrese x para salir: ')
#     cuentos = ['En', 'un', 'lugar', 'de', 'la', 'Mancha,', 'de', 'cuyo', 'nombre', 'no', 'quiero', 'acordarme,', 'no', 'ha', 'mucho', 'tiempo', 'que', 'vivía', 'un', 'hidalgo', 'de', 'los', 'de', 'lanza', 'en', 'astillero,', 'adarga', 'antigua,', 'rocín', 'flaco', 'y', 'galgo', 'corredor.']
#     try:
#         indice = cuentos.index(palabra)
#         print(f'La palabra "{palabra}" está en la posición {indice}')
#     except ValueError:
#         print('La palabra no se encontró')







# # Busca la posición del número en la lista que cambia
# def aleatorio(valor):
#     p = print
#     import random
#     lista = [1,2,3,4,5,6,7,8,9,0]
#     random.shuffle(lista)

#     for k, elemento in enumerate(lista):
#         if elemento == valor:
#             print(f'Encontrado en la posición {k}')
#             break
#         else:
#             p('No encotrado')
# aleatorio(3)








# #crear una lista enumerada a partir de un la lista
# lista = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo', 'Jamón','Carne','Tocino','Queso']
# string = [str(idx + 1) + '. ' + elemento for idx, elemento in enumerate(lista)]
# string = '\n'.join(string)
# string += '\n'
# print(string)
# # Salida
# # 1. Tomate
# # 2. Champiñones
# # 3. Aceituna
# # 4. Cebolla
# # 5. Pollo
# # 6. Jamón
# # 7. Carne
# # 8. Tocino
# # 9. Queso










# # Imprime listado de letra y alternativa
# alternativas = ['nombre','apellido','edad','altura']
# letras = ['A','B','C','D']
# for l, a in zip(letras, alternativas):
#     print(f'{l}. {a}')
# # Salida:
# # A. nombre
# # B. apellido
# # C. edad
# # D. altura










# # Elección con not in y while
# opciones = [1,2,3,4,5,6,7,8,9,0]
# eleccion = int(input('Ingrese una opción: '))

# while eleccion not in opciones:
#     eleccion = int(input('Opción no válida, ingrese una de las opciones válidas: '))
# print(f'El numero {eleccion} está en la lista')










# #Convertir una lista de tuplas en diccionario
# lista_tuplas = [('a', 25), ('b', 31), ('c', 'hello'), ('e', 'feo'), ('f', 'malo'), ('g', 'bueno')]
# lista2 = dict(lista_tuplas)
# print(lista2) # diccionario 