def agregar_ingredientes(pizza_base, eleccion):
    disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo', 'Jamón','Carne','Tocino','Queso']
    if eleccion <= 0 or eleccion > len(disponibles):
        print('>>> Ingrediente no existe')
    else:
        nuevo_ingrediente = disponibles[eleccion - 1]
        if nuevo_ingrediente in pizza_base['ingredientes']:
            print('>>> El ingrediente ya existe')
        else:
            pizza_base['ingredientes'].append(nuevo_ingrediente)
            print(f'>>> Se ha agredado {nuevo_ingrediente}')
    return pizza_base

# if __name__ == '__main__':
#     pizza_base_prueba = {
#     'masa': 'Masa Tradicional',
#     'salsa': 'Salsa de Tomate',
#     'ingredientes': ['Queso']
#     }
#     disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo', 'Jamón','Carne','Tocino','Queso']
#     string_pregunta = [str(idx + 1) + '. ' + ingre for idx, ingre in enumerate(disponibles)]
#     string_pregunta = '\n'.join(string_pregunta)
#     string_pregunta += '\n'

#     try: 
#         eleccion = int(input(f'''Seleccione su ingrediente:\n
# {string_pregunta}> '''))
#     except ValueError:
#         print('Debe ingresar solo números')
#     else:
#         pizza_base = agregar_ingredientes(pizza_base_prueba, eleccion)
#         print(pizza_base_prueba)