def calculo_tiempo(pizza_base):
    n_ingredientes = len(pizza_base['ingredientes'])
    tiempo = 20 + n_ingredientes * 2
    return tiempo

if __name__ == '__main__':
    pizza_base_prueba = {
    'masa': 'Masa Tradicional',
    'salsa': 'Salsa de Tomate',
    'ingredientes': ['Tomate','Champiñones','Aceituna','Cebolla']
    }
    print(calculo_tiempo(pizza_base_prueba))