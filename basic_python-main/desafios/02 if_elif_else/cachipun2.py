import random

#Se solicita la jugada, formatea a minúscula y la muestra en pantalla
jugada_usuario = input('Escriba su jugada:\n- Piedra \n- Papel \n- Tijera \n')
jugada_usuario = jugada_usuario.lower()
print(f'\nTú jugaste {jugada_usuario}')

#La CPU elige su opción y la presenta en pantalla
jugada_cpu = random.choice(['piedra', 'papel', 'tijeras'])
print(f'Computador eligió {jugada_cpu}')


#Evalucación usuario piedra
if jugada_usuario == 'piedra': 
	if jugada_cpu == 'piedra': 
		print('Empate: ambos elijeron piedra')
	elif jugada_cpu == 'papel':
		print('Perdiste!! papel gana a piedra')
	else: 
		print('Ganaste!!: piedra gana a tijera')


#Evalucación usuario papel
elif jugada_usuario == 'papel':
	if jugada_cpu == 'piedra': 
		print('Ganaste!!: papel gana a piedra')
	elif jugada_cpu == 'papel':
		print('Empate: ambos elijeron papel')
	else:
		print('Perdiste!! papel pierde con tijera')

#Evalucación usuario tijera
elif jugada_usuario == 'tijera':
	if jugada_cpu == 'piedra': 
		print('Perdiste!! tijera pierde contra pierda')
	elif jugada_cpu == 'papel':
		print('Ganaste!!: papel gana a tijera')
	else: 
		print('Empate: ambos elijieron tijera')

#En caso de no ingresar un valor válido
else:
	print ('Argumento inválido: Debe ser piedra, papel o tijera.')
