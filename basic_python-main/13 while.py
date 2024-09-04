# def main():
# # esCorrecta = False
# # while esCorrecta != True:
#     while True:
#         # 1. Le pido la nueva contraseña la usuario
#         password = getpass.getpass('Ingrese una contraseña: ')
#         print(f'Password ingresado: {password}')
#         # Valido la contraseña con la función "validarPassword"
#         esCorrecta = validarPassword(password) 
#         # Si la contraseña es incorretca, repite el ciclo. Si está bien, salgo del ciclo con break
#         if esCorrecta:
#             break # Salir del ciclo
#     print('Bienvenido!') # Fuera del ciclo
# main()








# numero = None
# while numero is None:
#     try:
#         numero = int(input("Ingresa un número: "))
#     except ValueError:
#         print("Eso no es un número válido.")







# import sys #Permite ingresar datos desde la consonla
# def sigma():
#     numero = int(sys.argv[1]) #Indica qué atributo tomará, el primero junto al nombre 
#     i = 1 #inicar iterador
#     suma = 0
#     while i <= numero: # condición 
#         suma += i
#         i += 1 # Incremento 
#     print(suma) 
# sigma()








# # Elección con not in y while
# opciones = [1,2,3,4,5,6,7,8,9,0]
# eleccion = int(input('Ingrese una opción: '))

# while eleccion not in opciones:
#     eleccion = int(input('Opción no válida, ingrese una de las opciones válidas: '))
# print(f'El numero {eleccion} está en la lista')









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
