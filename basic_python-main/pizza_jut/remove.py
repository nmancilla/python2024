# def quitar_ingredientes(ingredientes, eleccion):
#     disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo', 'Jamón','Carne','Tocino','Queso']
#     quitar = disponibles[eleccion - 1]
#     if quitar in ingredientes['ingredientes']:
#         ingredientes['ingredientes'].remove(quitar)
#         print(f'Se ha quitado el ingrediente {quitar}')
#     elif len(ingredientes['ingredientes']) == 0:
#         print('No hay ningún ingrediente que quitar')
#     else:
#         print('No se puede quitar ingrediente, porque no está incluido')
#     return ingredientes


# if __name__ == '__main__':
#     ingredientes_prueba = {
#     'masa': 'Masa Tradicional',
#     'salsa': 'Salsa de Tomate',
#     'ingredientes': ['Queso']
#     }

#     eleccion = int(input('''Seleccione qué ingrediente quitar:
#     1. Tomate
#     2. Champiñones
#     3. Aceitunas
#     4. Cebolla
#     5. Pollo
#     6. Jamón
#     7. Carne
#     8. Tocino
#     9. Queso
#     > '''))

#     ingredientes = quitar_ingredientes(ingredientes_prueba, eleccion)
#     print(ingredientes)









def quitar_ingredientes(pizza_base):
    if len(pizza_base['ingredientes']) == 0:
        print('No hay ningún ingrediente que quitar')
    else:
        string_pregunta = [str(idx + 1) + '. ' + ingre for idx, ingre in enumerate(pizza_base['ingredientes'])]
        string_pregunta = '\n'.join(string_pregunta)
        string_pregunta += '\n\n'
        print('Elija un ingrediente para eliminar: ')
        eleccion = int(input(string_pregunta))
        if eleccion < 0 or eleccion > len(pizza_base['ingredientes']):
            print('>>> Ese ingrediente no está en la pizza')
            return
        quitar = pizza_base['ingredientes'][eleccion - 1]
        print(f'>>> Se ha quitado el ingrediente {quitar}')
        pizza_base['ingredientes'].remove(quitar)
    return pizza_base

if __name__ == '__main__':
    ingredientes_prueba = {
    'masa': 'Masa Tradicional',
    'salsa': 'Salsa de Tomate',
    'ingredientes': ['Queso', 'Tomate', 'Champiñon']
    }
    ingredientes = quitar_ingredientes(ingredientes_prueba)
    print(ingredientes)










# def drop_ingrediente(pizza):
#     string_pregunta = [str(idx + 1) + '. ' + ingre for idx, ingre in enumerate(pizza['ingredientes'])]
#     string_pregunta = '\n'.join(string_pregunta)
#     string_pregunta += '\n\n'
#     print('Elija un ingrediente para eliminar: ')
#     eleccion = int(input(string_pregunta))
#     if eleccion < 0 or eleccion > len(pizza['ingredientes']):
#         print('Ese ingrediente no está en la pizza')
#         return
#     ingrediente_electo = pizza['ingredientes'][eleccion - 1]
#     print(f'Se ha quitado el ingrediente {pizza["ingredientes"][eleccion -1 ]}')
#     pizza['ingredientes'] = [item for item in pizza['ingredientes'] if item != ingrediente_electo]
#     return pizza

# if __name__ == '__main__':
#     ingredientes_prueba = {
#     'masa': 'Masa Tradicional',
#     'salsa': 'Salsa de Tomate',
#     'ingredientes': ['Queso', 'Tomate', 'Champiñon']
#     }
#     ingredientes = drop_ingrediente(ingredientes_prueba)
#     print(ingredientes)