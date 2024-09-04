import sys

def word_count():
    #1. Obtener el nombre del archivo
    nombre_archivo = sys.argv[1]
    #2. Leer el contenido del archivo
    with open(nombre_archivo, 'r') as file:
        texto = file.read()
    #3. Contamos las letras totales
    texto_sin_espacios = [letra for letra in texto if letra != ' ']
    print(f'El archivo hay (sin contar espacios) {len(texto_sin_espacios)} letras.')
    #3.1 Contar letras sin duplicar
    caracteres = set([letra for letra in texto])
    print(f'En ńumero de caracteres diferentes es: {len(caracteres)}')
    #3.5 Eliminar duplicados
    lista_sin_duplicados = list(set(texto.split(' ')))
    #4. Contar palabras sin duplicar
    num_palabras = len(lista_sin_duplicados)
    print(f'Hay {num_palabras} palabras no duplicadas')
#word_count()


def conversiones():
    tasa_sol_peru = float(sys.argv[1])
    tasa_peso_arg = float(sys.argv[2])
    tasa_dolar_ame = float(sys.argv[3])
    peso_chileno = int(sys.argv[4])
    print(f'''
    Los {peso_chileno} pesos equivalen a:
    {peso_chileno * tasa_sol_peru} Soles
    {peso_chileno * tasa_peso_arg} Pesos Argentinos
    {peso_chileno * tasa_dolar_ame} Dólares
    ''')
#conversiones()


# def recordatorios():
#     recordatorios = [
#         ['2021-01-01', "11:00", "Levantarse y ejercitar"],
#         ['2021-05-01', "15:00", "No trabajar"],
#         ['2021-07-15', "13:00", "No hacer nada es feriado"],
#         ['2021-09-18', "16:00", "Ramadas"],
#         ['2021-12-25', "00:00", "Navidad"]
#     ]
#     #1. Agregar
#     #evento_nuevo = ['2021-02-02', '06:00', 'Empezar el año']
#     #recordatorios = [recordatorios[0], evento_nuevo] + recordatorios[1:] #desde el 1 en adelante
#     recordatorios.insert(1, ['2021-01-02', '06:00', 'Empezar el año'])
#     # #2. Editar
#     recordatorios[2][0] = '2021-07-16'
#     # #3 Eliminar
#     del recordatorios[2]
#     # 4 Agregar cena navidad
#     recordatorios.insert(4, ['2021-12-24', '22:00', 'Cena de Navidad'])
#     # 5 Agregar cena año nuevo
#     recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])
#     #Imprimir
#     for recordatorio in recordatorios:
#         print(recordatorio)
# recordatorios()
