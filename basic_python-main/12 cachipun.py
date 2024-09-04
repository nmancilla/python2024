import random

''' Vamos a jugar cachipún con el usuario'''

# 1. Vamos a pedir la jugada del usuario
jugada_usuario = input('Ingrese su jugada:\n1: Piedra \n2: Papel \n3: Tijera \n')

#1.2 
if jugada_usuario == '1':
  print('USTED eligió piedra')
elif jugada_usuario == '2':
  print('USTED eligió papél')
elif jugada_usuario == '3':
  print('USTED eligió tijera')

#2. Geneara la juagada del computador
jugada_cpu = random.randint(1, 3)

#3- Transformo la jugada a string la jugada del cop
jugada_cpu = str(jugada_cpu)


#3.2
if jugada_cpu == '1':
  print('CPU eligió piedra')
elif jugada_cpu == '2':
  print('CPU eligió papél')
elif jugada_cpu == '3':
  print('CPU eligió tijera')

#print('Jugada del computador: ' + jugada_cpu)

#4. Resolvermos quien gana
if jugada_usuario == '1': 
  if jugada_cpu == '1': 
    print('Empate: ambos elijeron piedra')
  elif jugada_cpu == '2':
    print('Gana CPU: Papel contra Piedra')
  else: #Usario eligió jugada_cpu == '3'
    print('Usted Gana: Piedra contra Tijera')

elif jugada_usuario == '2':
  if jugada_cpu == '1': 
    print('Usted gana: papel contra piedra')
  elif jugada_cpu == '2':
    print('Empate: ambos elijeron papel')
  else: #Usario eligió jugada_cpu == '3'
    print('Gana CPU: Papel contra tijera')

elif jugada_usuario == '3':
  if jugada_cpu == '1': 
    print('Gana CPU: tijera contra pierda')
  elif jugada_cpu == '2':
    print('Usted gana: papel contra tijera')
  else: #Usario eligió jugada_cpu == '3'
    print('Empate: ambos elijieron tijera')

else:
  print ('Opción no válida')


