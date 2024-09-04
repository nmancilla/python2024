# Tuplas: Par ordenado inmutable 
# No se pueden modificar partes de ella, en caso de querer actualizarlo,
# se debe modificar la tupla completa





# dias = ('lun', 'mar', 'mier') #la tupla es innmutable
# dias[2] = 'jue'  #TypeError: 'tuple' object does not support item assignment (no se puede mutar una tupla)

# dias = tuple(list(dias) + ['jue'])

# dias  += ('jojo', 'jeje') #no modifica, sino que crea una y la asigna la reasigna a dias
# print(dias)








# votacion = ['Trump', 'Biden', 'Biden', 'Putin', 'Biden', 'Trump', 'Biden', 'Pedro Pascal', 'Pikachu', 'Trump', 'Putin']
# #votacion = list(set(votacion))
# votacion.sort()
# print(votacion) #me dice cuales son las opciones

# '''
# Quiero armar algo así:
# {
#     'Trump': 45,
#     'Biden': 40
#     ...
# }
# '''

# resultados = {}
# for voto in votacion:
#     if voto in resultados.keys():
#         resultados[voto] += 1
#     else:
#         resultados[voto] = 1
# print(resultados)






# def buenos_modales(nombre = 'Anonimo'): #Valor por defecto cuando está sin argumento (nombre = parámetro, entrada)
#     hola = 'Buenos dias ' + nombre
#     chao = 'Nos vemos, ' + nombre
#     return hola, chao # retorna una tupla

# #Desempaquetar la tupla
# saludo, adios = buenos_modales('Cristian') 
# '''
# palabras = buenos_modales('Matias')
# saludo = palabras[0]
# adios = palabras[1]
# '''
# print(saludo)
# print(adios)








# #Unpacking o desempaquetamiento
# tupla = ('enero', 2021)
# print(type(tupla))
# print(tupla)

# #Desepaquetando
# fecha, yrs = tupla
# print(fecha) #str
# print(yrs) # int







# #Set
# # La principal diferencia entre los diccionarios y los sets,
# # es que los sets solo tienen valores, no tienen claves.

# muchos_animales = {
#     'Gato', 'Perro', 'Tortuga',
#     'Gato', 'Perro', 'Tortuga',
#     'Gato', 'Perro', 'Tortuga',
#     'Gato', 'Perro', 'Tortuga',
#     'Hurón', 'Hamster', 'Erizo de Tierra'
# }

# print(set(muchos_animales)) #Solo valores únicos






