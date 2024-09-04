def cambiar_tipo_masa(pizza_base, eleccion):
    if eleccion == '1':
        pizza_base['masa'] = 'Masa Tradicional'
    elif eleccion == '2':
        pizza_base['masa'] = 'Masa Delgada'
    elif eleccion == '3':
        pizza_base['masa'] = 'Masa con bordes de queso'
    if eleccion in ['1', '2', '3']:
        print(f">>> Su masa sido cambiada a: {pizza_base['masa']}")
    else:
        print('>>> No se ha cambiado su tipo de masa')
    return pizza_base # Retorna pizza_base con la nueva masa

if __name__ == '__main__':
    pizza_base_prueba = {
    'masa': 'Masa Tradicional',
    'salsa': 'Salsa de Tomate',
    'ingredientes': []
    }
    eleccion = input('''
    Escoja el tipo de masa:
    1. Masa Tradicional
    2. Masa Delgasa
    3. Masa con bordes de queso
    ''')
    pizza_base  = cambiar_tipo_masa(pizza_base_prueba, eleccion)
    print(pizza_base)
