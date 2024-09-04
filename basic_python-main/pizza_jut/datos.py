principal = '''
        ¿Qué desea realizar?
        1. Cambiar tipo de masa
        2. Cambiar tipo de salsa
        3. Agregar ingredientes
        4. Quitar ingredientes
        5. Ordenar con los ingredientes actuales
        6. Consultar ingredientes
        0. Salir
        
        Otro número cancelará el pedido
        > '''

tipo_de_masa = '''
        Escoja el tipo de masa:
        1. Masa Tradicional
        2. Masa Delgada
        3. Masa con bordes de queso
        > '''

salsa = '''
        Elija el tipo de Salsa:
        1. Salsa de Tomate
        2. Salsa Alfredo
        3. Salsa Barbecue
        4. Salsa Pesto
        > '''

ingredientes_disponibles = '''
        Seleccione su Ingrediente:
        1. Tomate
        2. Champiñones
        3. Aceituna
        4. Cebolla
        5. Pollo
        6. Jamón
        7. Carne
        8. Tocino
        9. Queso
        > '''

ingredientes = {
        'masa': 'Masa Tradicional',
        'salsa': 'Salsa de Tomate',
        'ingredientes': []
}