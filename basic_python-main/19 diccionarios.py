# # #Métodos
# diccionario = {
#     'a': 25,
#     'b': 31,
#     'c': "hello",
#     'e': 'feo',
#     'f': 'malo',
#     'g': 'bueno'
# }
# print(diccionario.keys())                #Muestra una LISTA con solo las llaves
# print(diccionario.values())              #Muestra una LISTA con solo las llaves
# print(diccionario.items())               #Muestra una LISTA con pares clave-valor
# # diccionario = list(diccionario.items()) #Transforma en lista de tuplas
# print(diccionario)
# print(diccionario['c'])                   # Ver el valor de la llave c (hello)
# diccionario['g'] = 'Bondadoso'            # Cambio el valor de la llave g (sobrescribe)
# diccionario['h'] = 'Terrible'             # agregar una nueva llave y valor . La llave debe ser única
# del diccionario['h']                      # Elimina la clave
# print(diccionario)




# # Acceder al diccionario directo
# diccionario = {
#     "a": 25,
#     "b": 31,
#     "c": "hello",
#     "c": "chao" # Cuando la clave está duplicada, toma el útimo valor
# }
# print(diccionario['c']) # Se accede por la clave






# # Acceder al diccionario usando in
# def poliglota(nombre, idioma):
#     idiomas = {
#         'ingles': 'Hello, how are you!', 
#         'sueco': 'Hejsan, hur är det!',
#         'aleman': 'Hallo, wie geht es du!'
#     }
    
#     if idioma in idiomas.keys():
#         print(f'{idiomas[idioma]}, {nombre.capitalize()}')
#     else:
#         print('No entiendo el idioma')
# poliglota('carlos', 'sueco')







# # Get para informar datos que no están
# diccionario = {
#     'a': 'bueno',
#     'b': 'malo',
#     'c': 'feo',
# }
# # print(diccionario['d']) # Genera error, para evitarlo:
# print(diccionario.get('a', 'no definido')) # como existe, imprime bueno
# print(diccionario.get('d', 'no definido')) # como NO existe, imprime no definido







# #Get
# diccionario = {
#     'a': 25,
#     'b': 31,
#     'c': "hello",
#     'e': 'feo',
#     'f': 'malo',
#     'g': 'bueno'
# }
# consulta = input('Ingrese un dato: ')
# print(diccionario.get(f'{consulta}', 'No se encuentra')) #Muestra el valor, sino, No se encuentra








# #Agregando y modificando elementos
# diccionario = {
#     'a': 25,
#     'b': 31,
#     'c': "hello"
# }

# diccionario['d'] = 'Chao' # Se agrega d
# diccionario['c'] = 'Hola' # Modifica c
# del diccionario['a']  # Elimino la clave a sin mostrarlo
# print(diccionario.pop('b')) # Elimino y muestro el valor eliminado









# #Uniendo diccionarios, concatenando
# diccionario_a = {
#     'a': 25,
#     'b': 31,
#     'c': "hello"
# }
# diccionario_b = {
#     'e': 'feo',
#     'f': 'malo',
#     'g': 'bueno'
# }
# diccionario_a.update(diccionario_b)
# print(diccionario_a)









# #Convertir un diccinario en una lista de los valores:
# perro = {
#     'raza': 'cocker',
#     'nombre': 'Joe',
#     'edad': 8
# }
# nueva = list(perro.values())
# print(nueva) # Salida: ['cocker', 'Joe', 8]







# #Convertir un diccinario en una lista de tuplas:
# perro = {
#     'raza': 'cocker',
#     'nombre': 'Joe',
#     'edad': 8
# }
# nueva = list(perro.items())
# print(nueva) # Salida: [('raza', 'cocker'), ('nombre', 'Joe'), ('edad', 8)]






# # Convertir una lista de tuplas en diccionario:
# lista = [('raza', 'cocker'), ('nombre', 'Joe'), ('edad', 8)]
# diccionario = dict(lista)
# print(diccionario)









# # Convierte dos listas en un diccionario:
# claves = ['nombre','apellido','edad','altura']
# valores = ['Juan','Pérez', 33, 1.75]
# print({k:v for k,v in zip(claves, valores)})











# # Iterando:
# perro = {
#     'raza': 'cocker',
#     'nombre': 'Joe',
#     'edad': 8
# }

# #Iterando por llave
# for llave in perro.keys():
#     print(llave)

# #Iterando por values
# for valor in perro.values():
#     print(valor)

# #Iterando por ambos (lista de pares)
# for k, v in perro.items():
#     print(f'El valor de la llave {k} es: {v}')






# # Iterando un diccionario
# perro = {
#     'raza': 'cocker',
#     'nombre': 'Joe',
#     'edad': 8
# }

# for llave, valor in perro.items():
#     print(f'La llave: {llave} tiene el valor: {valor}') #iterar el diccionario








# # Consultado diccionarios
# semana = {
#     'lunes': 2,
#     'martes': 2,
#     'miercoles': 4,
#     'jueves': 4,
#     'viernes': 2
# }

# def mostrar_semana(semana):
#     for llave, valor in semana.items():
#         if valor == 2:
#             print(f'el dia {llave} fue un dia CORTO')
#         else:
#             print(f'el dia {llave} fue un dia LARGO')
# mostrar_semana(semana)


















# # Iterando una lista con diccionario:
# stop = None
# diccionario_personajes = []
# n = 0

# while stop != 'x':
#     nombre = input('\nNombre: ')
#     planeta = input('Planeta: ')
#     poder = input('Habilidad: ')
#     stop = input('Digitar x para detener: ')

#     personaje = {
#         'nombre': nombre,
#         'planeta': planeta,
#         'poder': poder
#     }
#     diccionario_personajes.append(personaje)

# for personaje in diccionario_personajes:
#     n += 1
#     print(f'\nPersonaje {n}:')
#     for llave, valor in personaje.items():
#         print(f'Su {llave} es {valor}')








# # Accediendo a datos dentro de una lista de diccionarios
# destinos = [
#     {
#         'nombre': 'Argentina',
#         'prefijo': 54,
#         'ciudades': ['BS AS', 'Cordova', 'Mendoza', 'Jumin']
#     },
#     {
#         'nombre': 'Suecia',
#         'prefijo': 47,
#         'ciudades': ['Estocolmo', 'Gotermburno', 'Malmo', 'Kiruna']
#     }
# ]
# print(destinos[0]['ciudades'][1]) # Cordova
# print(destinos[1]['ciudades'][2]) # Malmo








# # Extrayenodo datos puntales de una lista de diccionarios
# usuarios = [
# {'nombre': 'Page',
# 'apellido': 'Stappard',
# 'email': 'pstappard0@java.com',
# 'genero': 'Bigender'
# },

# {'nombre': 'Alli',
# 'apellido': 'Truckell',
# 'email': 'atruckell1@lulu.com',
# 'genero': 'Agender'
# },

# {'nombre': 'Nissy',
# 'apellido': 'Dell Casa',
# 'email': 'ndellcasa2@godaddy.com',
# 'genero': 'Female'
# }]

# for usuario in usuarios:
#     nombre = usuario.get('nombre')
#     apellido = usuario.get('apellido')
#     email = usuario.get('email')
#     genero = usuario.get('genero')

#     print(f'name: {nombre}, lastname: {apellido}, email: {email}, genre: {genero} ')








# # Elegir un valor random de una clave elegida
# import random

# opciones = {
#     'bas':  [1,2,3],
#     'inter': [4,5,6],
#     'avan': [7,8,9]
# }

# eleccion = input('Elija una opción (bas, inter, avan): ')
# num = random.choice(opciones[eleccion])
# print(num)







# # imprime en formato Json en terminal
# import json
# usuarios = [
# {'nombre': 'Page',
# 'apellido': 'Stappard',
# 'email': 'pstappard0@java.com',
# 'genero': 'Bigender'
# },

# {'nombre': 'Alli',
# 'apellido': 'Truckell',
# 'email': 'atruckell1@lulu.com',
# 'genero': 'Agender'
# },

# {'nombre': 'Nissy',
# 'apellido': 'Dell Casa',
# 'email': 'ndellcasa2@godaddy.com',
# 'genero': 'Female'
# }]

# print(json.dumps(usuarios, indent=4))








# # **kwargs (Argumentos de palabra clave):
# # **kwargs permite pasar un número variable de argumentos de palabra clave a una función.
# # Los argumentos se recopilan en un diccionario dentro de la función.
# # Útil cuando queremos manejar argumentos con nombres específicos.

# def mostrar_info(**kwargs):
#     print(kwargs) # Es un diccionario
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")


# mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")
# # Salida:
# # {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
# # nombre: Juan
# # edad: 30
# # ciudad: Madrid
