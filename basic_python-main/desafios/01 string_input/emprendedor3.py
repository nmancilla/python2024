'''
Varibles
--------

precio_sus:       Precio de Suscripción
num_usu_norm:     Número de Usuarios Normales
gastos_tot:       Gastos Totales
util_ano_anter:   Utilidad año anterior
razon:            Razón entre la utilidad actual y la del año anterior

'''

print('-'*29)
print ('Calculadora de rentabilidad 3')
print('-'*29)

#Adevertencia
print('(Ingresar solo números enteros)')

#Solicitud de datos
precio_sus = int(input('Ingrese precio de suscripción: '))
num_usu_norm = int(input('Ingrese número de Usuarios Normales: '))
gastos_tot = int(input('Ingrese gasto total: '))
util_ano_anter = int(input('Ingrese la utilidad del año anterior: '))

#Cálculos
util = int((precio_sus * num_usu_norm) - gastos_tot)
razon = round((util / util_ano_anter), 2)

#Presentación
print('\n')
print(f'La utilidad actual es: {util}')
print(f'La de año anterior es: {util_ano_anter}\n')
print(f'Razón entre la utilidad actual y la del año anterior es: {razon}')
