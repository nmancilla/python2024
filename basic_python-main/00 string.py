# # string multilinea con '''
# nombre = '''Juan
# Manuel
# Pérez
# Toro'''
# print(nombre)








# # Concatenando
# print('Carlos ' + 'Santana')
# print('Carlos ' * 3)








# # Salto de linea usando \n
# print("hola\na\ntodos")









# # Uso de comilla simple en string
# etiqueta = '''<a hred="#">Región O'higgins</a>'''
# etiquete = """<a hred="#">Región O'higgins</a>"""
# etiqueti = '<a hred="#">Región O\'higgins</a>'
# print(etiqueta)
# print(etiquete)
# print(etiqueti)









# # Métodos de string
# print('Nirvana canta '.count('an'))                   # Cuenta cuantas veces sale an
# print(len('Grupo musical de metal  5'))               # Cuenta llos carácteres inculuido espacios
# print('santana'.upper())                              # Todas en máyusculas
# print('HolA cOmo EstÁS '.lower())                     # Todas en minúsculas
# print('carlos santana'.title())                       # Mayúscula las primeras letras
# print('hola a todos'.capitalize())                    # Mayúscula primera letra
# print(' Hola a todo, cómo están '.strip())            # Elimina los espacios al final o al principio
# print('Hola mundo'.replace('o', 'x'))                 # Eeemplaza las ocurrencias
# print(' -> '.join(['papel', 'piedra', 'tijera']))     # Une elementos con el string









# # Separador de palabra usando espacio y convertirlo en list
# texto = "Hola, ¿cómo estás?"
# palabras = texto.split()  # El separador por defecto es el espacio en blanco
# print(palabras)  # Salida: ['Hola,', '¿cómo', 'estás?']







# # Separador usando un # y convertirlo en list
# aaa = "carlos#santana#cantante#de#musica"
# separado = aaa.split('#')  # Usando la coma como separador
# print(separado) # Salida: ['carlos', 'santana', 'cantante', 'de', 'musica']