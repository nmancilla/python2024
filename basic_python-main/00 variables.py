# #Tipos de variables:
# variable = "Hola Mundo"
# print(type(variable))  # Salida: <class 'str'>

# numero = 42
# print(type(numero))  # Salida: <class 'int'>

# flotante = 4.32
# print(type(flotante)) # Salida: <class 'bool'>

# lista = [1, 2, 3]
# print(type(lista))  # Salida: <class 'list'>

# booleano = False
# print(type(booleano)) # Salida: <class 'bool'>








# Variables
# Python buscará si existe dicha variable en su propio scope; y en caso de existir utilizará dicho valor, 
# en caso contrario escalará a un ambiente superior
# La manera de poder utilizar una variable local en el ambiente global es mediante return,
# la que viene a ser la conexión entre el scope local de una función y el ambiente local.

# continent = 'South America'  # Definida en ambiente global
# def get_continent():
#     print(continent) # Contiente no está definida en el ambiente local o en su scope
# get_continent() # Imprime igual South America xq la busca en su ambiente superior






# # # Modificar una variable global desde un entorno local. NO recomendado
# continent = 'South America' # Varianble global
# def get_continent():
#     global continent
#     continent = 'Africa' # Modifica la varible global

# get_continent() # Se ejecuta la modifcación
# print(continent)

