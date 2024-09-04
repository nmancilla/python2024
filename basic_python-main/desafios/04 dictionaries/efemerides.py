def transformar_fecha():
    meses = {
        '1': 'enero', '2': 'febrero', '3': 'marzo', '4': 'abril',
        '5': 'mayo','6': 'junio', '7': 'julio', '8': 'agosto',
        '9': 'septiembre', '10': 'octubtre', '11': 'noviembre', '12': 'diciembre'
    }
    f_original = input('Ingrese una fecha: ')
    if '/' in f_original:
        f_array = f_original.split('/')
        f_nueva = f_array[0] + ' de ' + meses[f_array[1]]
        efemerides(f_nueva)
    else:
        efemerides(f_original)

    #signo_raro = first([signo in f_original for signo in ['.', '/', '-']], None) ???

def efemerides(f_original):
    efemerides = {'1 de enero': 'Año Nuevo',
    '27 de febrero': 'Terremoto en Chile',
    '8 de marzo': 'Día de la Mujer',
    '21 de mayo': 'Glorias Navales',
    '18 de septiembre': 'Fiestas Patrias',
    '19 de septiembre': 'Glorias del Ejercito',
    '25 de diciembre': 'Navidad'
    }
    #print(f'Efemérides: {efemerides[f_original]}') #Imprime el efemeride
    print(efemerides.get(f'{f_original}', 'No hay enventos para esta fecha!'))

transformar_fecha()