def agregar_salsa(pizza_base, eleccion):
    # Salsa de Tomate, Salsa Alfredo, Salsa Barbecue, Salsa Pesto
    if eleccion == '1':
        pizza_base['salsa'] = 'Salsa de Tomate'
    elif eleccion == '2':
        pizza_base['salsa'] = 'Salsa Alfredo'
    elif eleccion == '3':
        pizza_base['salsa'] = 'Salsa Barbecue'
    elif eleccion == '4':
        pizza_base['salsa'] = 'Salsa Pesto'
    if eleccion in ['1', '2', '3', '4']:
        print(f'>>> Su salsa se cambió a {pizza_base["salsa"]}')
    else:
        print('>>>> No se ha cambiado su tipo de salsa')
    return pizza_base

if __name__ == '__main__':
    pizza_base_prueba= {
    'masa': 'Masa Tradicional',
    'salsa': 'Salsa de Tomate',
    'ingredientes': []
    }
    eleccion = input('''
        Elija el tipo de Salsa:
        1. Salsa de Tomate
        2. Salsa Alfredo
        3. Salsa Barbecue
        4. Salsa Pesto
        > ''')
    pizza_base = agregar_salsa(pizza_base_prueba, eleccion)
    print(pizza_base)










# # Otra forma, con el input dentro de la función
# def agregar_salsa(pizza_base):
#     disponibles = ['Salsa de Tomate', 'Salsa Alfredo', 'Salsa Barbecue', 'Salsa Pesto']
#     while True:
#         try:
#             eleccion = int(input('''
#             Elija el tipo de Salsa:
#             1. Salsa de Tomate
#             2. Salsa Alfredo
#             3. Salsa Barbecue
#             4. Salsa Pesto
#             > '''))
#             if eleccion < 1 or eleccion > 4:
#                 print('Eleccion no valida!!')
#             else:
#                 pizza_base['salsa'] = disponibles[eleccion - 1]
#                 break
#         except ValueError:
#             print('Error de ingreso, intente de nuevo!!')
#     print(f'Su salsa se cambió a {pizza_base["salsa"]}')
#     return pizza_base

# if __name__ == '__main__':
#     pizza_base_prueba = {
#     'masa': 'Masa Tradicional',
#     'salsa': 'Salsa de Tomate',
#     'ingredientes': []
#     }
#     pizza_base = agregar_salsa(pizza_base_prueba)
#     print(pizza_base)

