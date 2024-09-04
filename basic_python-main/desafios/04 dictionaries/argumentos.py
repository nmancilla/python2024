import sys
nombre = sys.argv[0]
apellido = sys.argv[1]

print(f'Mi nombre es {nombre}')
print(f'Mi apellido es {apellido}')
print(f'El nombre de este archivo es {sys.argv[0]}') #argumento cero es el nombre del archivo

print(type(sys.argv)) # <class 'list'>