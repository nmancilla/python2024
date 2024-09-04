def hanoi(num_discos, inicio='A', fin='C'):
  intermmedio = 'ABC'.replace(inicio, '').replace(fin, '')
  if num_discos < 2:
    raise Exception('Hanoi recesita al menos 2 discos')
  if num_discos == 2:
    print(f'1: {inicio} -> {intermmedio}')
    print(f'2: {inicio} -> {fin}')
    print(f'3: {intermmedio} -> {fin}') 
  else:
    hanoi(num_discos - 1, inicio, intermmedio)
    print(f'{num_discos}: {inicio} -> {fin}')
    hanoi(num_discos - 1 , intermmedio, fin)

hanoi(4)