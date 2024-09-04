# # Escribir en archivo
# cuento = '''En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
# no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
# adarga antigua, rocín flaco y galgo corredor.'''
# archivo = open('salida.txt', 'w')
# archivo.write(cuento) # Se cierra manualmente
# archivo.close()






# # Escribir en archivo (mejor opción)
# cuento = '''En un lugar de la Mancha, de cuyo nombre no quiero acordarme,
# no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,
# adarga antigua, rocín flaco y galgo corredor.'''
# with open('salida.txt', 'w') as f:
#     f.write(cuento) # Se cierra automáticamente al salir de bloque, si hay error, lo cierra