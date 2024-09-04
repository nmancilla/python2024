def mostrar_ingredientes(pizza_base):
    print('>>> Su pizza está preaprada así:')
    print(f'>>> Su masa es: {pizza_base["masa"]}')
    print(f'>>> Su salsa es: {pizza_base["salsa"]}')
    print(f'>>> Los ingredientes adicionales son: ')
    for ingrediente in pizza_base['ingredientes']:
        print(f' - {ingrediente}')

if __name__ == '__main__':
    pizza_base_prueba = {
    'masa': 'Masa Tradicional',
    'salsa': 'Salsa de Tomate',
    'ingredientes': ['Tomate','Champiñones','Aceituna','Cebolla']
    }
    mostrar_ingredientes(pizza_base_prueba)