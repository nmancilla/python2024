'''
Variables
---------
precio_suscr:   Precio de Suscripción
num_usuarios:   Número de Usuarios
gastos_tot:     Gastos Totales
'''

print('-'*29)
print ('Calculadora de rentabilidad 1')
print('-'*29)

#Adevertencia
print('(Ingresar solo números enteros)')

#Solicitud de datos
precio_suscr = int(input('Ingrese precio de suscripción: '))
num_usuarios = int(input('Ingrese número de usuarios: '))
gastos_tot = int(input('Ingrese gasto total: '))

#Cálculo formula
util = (precio_suscr * num_usuarios) - gastos_tot

print(f'La utilidad es: {util}')
