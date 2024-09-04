# # #Métodos listas
# cuentos = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete']
# numero = [1, 2, 3, 4, 5]
# # print(dir(cuentos)) #Ver los métodos de cuentos
# # cuentos.append('ocho') #inserta al final
# # cuentos.insert(2, 'tres coma cinco') #inserta en la posición 2
# # cuentos.pop(3) # posición 3 elimina y lo muestra
# # cuentos.remove('seis') # lo borra
# # cuentos.reverse()
# # cuentos.sort() # Ordena de mayor a menor o alfabéticamente
# # cuentos.sort(reverse = True) # Ordena de menor a mayor
# # cuentos = sorted([3,6,7,4,1]) # Ordena la lista que está a dentro mayor a menor
# # cuentos = sorted([3,6,7,4,1], reverse = True) # Menor a mator
# # print(cuentos.index('dos')) # entrega  la posición
# # cuentos = cuentos + ['hoho', 'jiji', 'eaea'] # Agrega
# # cuentos += ['hoho', 'jiji', 'eaea'] # Agrega
# # cuentos = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete'] * 3 # Multiplia por 3
# # cuentos[2] = 'hola' # Agrega hola en la posición 2

# print(cuentos)
# print(sum(numero)) # suma
# print(max(numero)) # el más grande
# print(min(numero)) # el menor






# # Elemento de una lista
# ciudades = ['Puerto Montt', 'Talaca', 'Valdivia', 'Santiago', 'Viña del Mar']
# #                  0            1          2           3            4
# print(ciudades[3]) #Santiago






# # Penúltimo de una lista
# def penultimo(lista):
#     largo = len(lista)
#     return print(lista[largo - 2]) # El largo de la lista menos 2

# penultimo(['Feña', 'Vivi', 'Max', 'Carlos', 'Esteban'])






# # La posición -2 que es la penúltima
# a = [1, 2, 3, 4, 5]
# print(a[-2]) # 4 es el penúltimo







# # Reversa
# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)





# # Selecciona un rango pero usando el índice, pero no considera el último
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# b = a[1:5] 
# print(b) # Salida: [2, 3, 4, 5]








# #Transformar texto en una lista
# texto = 'Don Quijote de la Mancha es una novela'
# texto_list = texto.split(' ')
# print(texto_list) # ['Don', 'Quijote', 'de', 'la', 'Mancha', 'es', 'una', 'novela']






# # Convertir una lista de tuplas en diccionarioL:
# lista = [('raza', 'cocker'), ('nombre', 'Joe'), ('edad', 8)]
# diccionario = dict(lista)
# print(diccionario)





