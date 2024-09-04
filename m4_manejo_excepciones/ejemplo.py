print('Juego de adivinar un número')
print('---------------------------\n')

num_secreto = 3

try:
    eleccion = int(input('Dime tu número: '))
    if eleccion == num_secreto:
        print('Has adivinado mago!')
    else: 
        print('Fallaste')
except ValueError: # Captura el error 
    print('Yapo, ingresa un número, no otra cosa!!!')

print('fin')


# AttributeError        Error en una referencia o asignación a un atributo.
# ImportError           Importar un módulo no encontrado.
# IndexError            Referenciar un índice fuera del rango posible en una secuencia.
# KeyError              Referenciar una clave no existente en un diccionario.
# MemoryError           Ejecución que consume toda la memoria disponible.
# NameError             Referenciar una variable no encontrada.
# TypeError             Aplicar una operación o función a un objeto de tipo incorrecto.
# ZeroDivisionError     Dividir por cero.