def calculadora_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC) y muestra la clasificación de la OMS."""
    try:
        peso = float(peso)
        altura = float(altura) / 100
        imc = peso / altura**2
        print(f'Su IMC es {imc:.2f}')

        clasif = 'La clasificación OMS es'
        if imc < 18.5:
            clasificacion = 'Bajo Peso'
        elif imc < 25:
            clasificacion = 'Adecuado'
        elif imc < 30:
            clasificacion = 'Sobrepeso'
        elif imc < 35:
            clasificacion = 'Obesidad Grado I'
        elif imc < 40:
            clasificacion = 'Obesidad Grado II'
        else:
            clasificacion = 'Obesidad Grado III'
        
        print(f'{clasif} {clasificacion}')
    except ValueError:
        print("Por favor, ingrese valores numéricos para peso y altura.")

print('*** Calculadora de IMC según OMS ***')
peso_usuario = input('Ingrese peso en kilos: ')
altura_usuario = input('Ingrese estatura en centímetros: ')

calculadora_imc(peso_usuario, altura_usuario)


# Optimizado por Copilot:
# Se renombró la función a calculadora_imc para seguir las convenciones de Python (snake_case).
# Se agregó un bloque try-except para manejar errores si los valores ingresados no son numéricos.
# Se eliminó la redundancia en los rangos de los elif al no repetir el límite inferior, ya que el flujo del programa no lo requiere.
# Se añadió un comentario de documentación al principio de la función para explicar su propósito.
# Se cambió la variable clasif por clasificacion dentro del bloque condicional para evitar repetir la misma cadena de texto.
