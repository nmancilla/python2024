'''
Variables
---------
precio_sus:     Precio de Suscripción
num_usu_norm:   Número de Usuarios Normales
num_usu_prem:   Número de Usuarios Premium
gastos_tot:     Gastos Totales
util:           Utilidad
'''

print('-'*29)
print ('Calculadora de rentabilidad 2')
print('-'*29)

#Adevertencia
print('(Ingresar solo números enteros)')

#Solicitud de datos
precio_sus = int(input('Ingrese precio de suscripción: '))
num_usu_norm = int(input('Ingrese número de Usuarios Normales: '))
num_usu_prem = int(input('Ingrese número de Usuarios Premium: '))
gastos_tot = int(input('Ingrese gasto total: '))

#Cálculos
util = int(((precio_sus * num_usu_norm) + (num_usu_prem * (precio_sus * 1.5))) - gastos_tot)


print(f'La utilidad es: {util}')
