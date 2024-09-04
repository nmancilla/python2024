'''
Variables:
peso    : corresponde al peso de la persona en Kg.
altura  : corresponde a la altura en metros.
imc     : EL valor del IMC, en [Kg/m2]
'''
'''
Tabla OMS:
< 18.5              Bajo Peso
[ 18.5, 25 [        Adecuado
[ 25, 30 [          Sobrepeso
[ 30, 35[           Obesidad Grado I
[ 35, 40 [          Obesidad Grado II
> 40                Obesidad Grado III
'''


def calculadoraImc(peso, altura):
    peso = float(peso)
    altura = float(altura)/100
    imc = (peso / (altura)**2)
    print(f'Su IMC es {imc:.2f}')
    
    clasif = 'La clasificación OMS es'
    
    if imc < 18.5:
        print(f'{clasif} Bajo Peso')
    elif 18.5 <= imc < 25:
        print(f'{clasif} Adecuado')
    elif 25 <= imc < 30:
        print(f'{clasif} Sobrepeso')
    elif 30 <= imc < 35:
        print(f'{clasif} Obesidad Grado I')
    elif 36 <= imc < 40:
        print(f'{clasif} Obesidad Grado II')
    else:
        print(f'{clasif} Obesidad Grado III')

print('*** Calculadora de IMC según OMS ***')
peso = input('Ingrese peso en kilos: ')
altura = input('Ingrese estatura en centímetro: ')

calculadoraImc(peso, altura)