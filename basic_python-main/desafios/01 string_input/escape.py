from math import sqrt

print('-'*34)
print ('Calculadora de velocidad de escape')
print('-'*34)

#Advertencia
print('(Se acepta el ingreso de numeros decimales)')

#Solicitud de datas
r = float(input('Ingrese el radio en Kilómetros: '))
g = float(input('Ingrese la constante g: '))

#Cálculos
ve = sqrt(2 * g * (r * 1000))

#Presentación
print(f'La velocidad de Escape es {round(ve, 2)} [m/s]')
