# Parámetro es cuando defino la función y 
# el argumento es lo que le paso cuando invoco a esta
# Principio DRY: Don't Repeat Yourself





# def buenos_modales(nombre = 'Anonimo'): #Valor por defecto cuando está sin argumento (nombre = parámetro, entrada)
#     hola = 'Buenos dias ' + nombre
#     chao = 'Nos vemos, ' + nombre
#     return hola, chao # es una tupla

# #Desempaquetar la tupla
# saludo, adios = buenos_modales('Cristian') 
# '''
# palabras = buenos_modales('Matias')
# saludo = palabras[0]
# adios = palabras[1]
# '''
# print(saludo)
# print(adios)




# # Función que solo imprime el menú y puede ser reutilizado
# def imprimir_menu():
#     print('Opciones: ')
#     print('1) De acuerdo')
#     print('2) En desacuerdo')
#     print('3) No me interesa')
# imprimir_menu() # Invocar a la función






# # Retorno de dos valores (Tupla)
# def cuadrado_cubo(base):
#     cuadrado = base**2
#     cubo = base**3
#     return cuadrado, cubo
# # Desempaquetadp
# valor_cuadrado, valor_cubo = cuadrado_cubo(2)
# print(valor_cuadrado)
# print(valor_cubo)







# #Función que recibe diccionario (estructuras de datos)
# precios = {
#     'Notebook': 700000,
#     'Teclado': 25000,
#     'Mouse': 12000,
#     'Monitor': 250000,
#     'Escritorio': 135000,
#     'Tarjeta de Video': 1500000
# }
# def filtrar(diccionario, umbral):
#     filtro = {k:v for k,v in diccionario.items() if v > umbral}
#     return filtro
# print (filtrar(precios, 300000))










# # Parámetro por defecto
# def elevar(base, exponente, redondear = False): #En caso de no existir el param, es False
#     if redondear:
#         valor = round(base**exponente, 2 )
#     else:
#         valor = base**exponente
#     return valor

# print(elevar(2, 3.6))
# print(elevar(2, 3.6, redondear = True))









# # *args (Argumentos posicionales): 
# # *args permite pasar un número variable de argumentos posicionales a una función.
# # Los argumentos se recopilan en una tupla dentro de la función.
# # Útil cuando no sabemos cuántos argumentos se pasarán.
# def suma(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# resultado = suma(1, 2, 3, 4)
# print(resultado)  # Salida: 10








# # **kwargs (Argumentos de palabra clave):
# # **kwargs permite pasar un número variable de argumentos de palabra clave a una función.
# # Los argumentos se recopilan en un diccionario dentro de la función.
# # Útil cuando queremos manejar argumentos con nombres específicos.
# def mostrar_info(**kwargs):
#     for clave, valor in kwargs.items():
#         print(f"{clave}: {valor}")

# mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")
# # Salida:
# # nombre: Juan
# # edad: 30
# # ciudad: Madrid











# # Entrega un diccionario con sus claves y valores poniendo cualquier numero de claves
# def get_multiple(diccionario, *claves):
#     return {clave: diccionario[clave] for clave in claves}

# diccionario_prueba = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5,
#     'six': 6
# }

# resultado = get_multiple(diccionario_prueba, 'two', 'six', 'one')
# print(resultado)
