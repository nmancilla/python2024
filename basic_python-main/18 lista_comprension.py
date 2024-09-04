# Listas por Comprehension
# [fórmula for variable in iterable]
# Empezamos por el ciclo. Para cada variable en el iterable, realiza la fórmula"

# lista1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18] # Lista por extensión
# lista2 = [num for num in range(0, 20, 2)] # Lista por comprehensión, la misma
# print(lista1)
# print(lista2)





# # Lista de numeros pares. 10 repeticiones
# n = 10
# lista_par = [2 * i+2 for i in range(n)]
# print(lista_par)






# # Escribe QUINA en los múltiplos de 5 y los agrega a una lista
# # (Método 1)
# lista = []
# for i in range(20): #(0,31,1)
#     if i % 5 == 0:
#         lista.append('QUINA')
#     else:
#         lista.append(i)
# print(lista)

# # (Método 2 con lista por comprehensión)
# lista = ['QUINA' if i % 5 == 0 else i for i in range(20)]
# # Se lee: para cada iteración i en el range(20), se aplica la formula 'QUINA' if i % 5 == 0 else i
# print(lista)







# # Para la lista valores, crear una lista si son divibles o no
# valores = [0,4,5,6,7,8,9]
# divisibles = []
# for valor in valores:
#     if valor % 2 == 0:
#         divisibles.append('Si')
#     else:
#         divisibles.append('No')
# print(divisibles)

# # Por comprensión
# valores = [0,4,5,6,7,8,9]
# divisibles = ['Si' if valor % 2 == 0 else 'No' for valor in valores]
# print(divisibles)







# # Crea lista de enlaces
# nombres = ['Home', 'Quienes Somos', 'Contacto']
# enlaces = ['<a href="#">' + nombre + '</a>' for nombre in nombres]
# print(enlaces)







# Concatena
# nombres = ['Chingao', 'Florimar', 'Onur', 'Hernesto Lisama', 'Lazlo', 'Isaura']
# saludos = ['Hola ' + nombre for nombre in nombres ]
# print(saludos)





# # Hacer una lista con los que su nombre es mayor que 5 lentas
# # [expresión for variable in iterable if condición ]
# grande = ['andrea', 'olga', 'armando', 'pedro', 'anastasia', 'orlando']
# grupo1 = [nombre for nombre in grande if len(nombre) > 5] 
# grupo2 = [nombre if len(nombre) > 5 else None for nombre in grande] # Agrega None, por lo que no sirve
# print(grupo1)
# print(grupo2)







# # Filtrar
# # [expresión for variable in iterable if condición ]
# lista = ['Lechugas', 'Tomates', 5, 10, True, False, True, 'Papas', 5.1, 45.2, 1, 2, 0]
# lista2 = [valor for valor in lista if type(valor) is str] # Por tipo
# lista3 = [valor for valor in lista if isinstance(valor, str)] # Si es una instancia de string
# print(lista2) 
# print(lista3)







# # # Filtrar
# # # [expresión for variable in iterable if condición ]
# ping = [120, 50, 600, 30, 90, 10, 200, 0, 500]
# resultado = ['Bien' if p <= 90 else 'mal' for p in ping]
# print(resultado)







# #agrega los mayores e iguales a mil
# # [expresión for variable in iterable if condición ]
# a = [100, 200, 1000, 5000, 10000, 10, 5000]
# b = [valor for valor in a if valor >= 1000]
# print(b)






# # [expresión for variable in iterable if condición ]
# minutos = [120, 50, 600, 30, 90, 10, 200, 0, 500]
# resultado = ['bien' if minuto <= 90 else 'mal' for minuto in minutos]
# print(resultado)






# seconds = [100, 50, 1000, 5000, 1000, 500]
# minuts = [numsec / 60 for numsec in seconds]
# print(minuts)








# rating = [50, 30, 45, 25, 55, 20]
# resultados = ['Bien ' if puntos >= 45 else 'mal' for puntos in rating ]
# print(resultados)
