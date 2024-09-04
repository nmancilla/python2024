# def imprimir_menu():
#     print('Opciones: ')
#     print('1). De acuerdo')
#     print('2). En desacuerdo')
#     print('3). No me interesa')

# preguntas = ['Enunciado Pregunta 1', 'Enunciado Pregunta 2','Enunciado Pregunta 3']
# respuestas = []
# # Hacer preguntas
# for p in preguntas:
#     print(p)
#     imprimir_menu()
#     respuestas.append(input('> '))
# print(f'La respuesta a la pregunta 1 fue {respuestas[0]}')
# print(f'La respuesta a la pregunta 2 fue {respuestas[1]}')
# print(f'La respuesta a la pregunta 3 fue {respuestas[2]}')
# print('Muchas gracias por responder la encuesta')









# preguntas = [
#     '¿Qué opina de eso?',
#     '¿Votaría por Mario para CORE',
#     '¿Sómos el curso favorito del profe?'
# ]
# respuestas = []
# dicc_respuestas = {
#         '1': 'Muy de acuerdo',
#         '2': 'En desacuerdo',
#         '3': 'Ni acuerdo ni en desacuerdo',
#         '4': 'De acuerdo',
#         '5': 'Muy de acuerdo'
# }

# def preguntar(pregunta):
#     print(pregunta)
#     opciones = '''
#         Seleccione una de las siguientes:
#         1. Muy de acuerdo
#         2. En desacuerdo
#         3. Ni acuerdo ni en desacuerdo
#         4. De acuerdo
#         5. Muy de acuerdo
#     '''
#     eleccion = input(opciones)
#     respuesta = dicc_respuestas.get(eleccion, 'N.S.N.R')
#     respuestas.append({
#         'pregunta': pregunta,
#         'respuesa': respuesta
#     })

# def main():
#     for pregunta in preguntas:
#         preguntar(pregunta)
#     print(respuestas)

# main()
