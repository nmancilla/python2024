# Para medir el remdimiento de un código.
# timeit desactiva temporalmente el recolector de basura y proporciona una 
# forma más precisa de medir el tiempo de ejecución

import timeit

codigo = """
lista = [1, 3, 5, 9, 9, 6]

def buscar1(valor_a_buscar):
    conjunto = set(lista)
    if valor_a_buscar in conjunto:
        print("¡Valor encontrado!")
    else:
        print("Valor no encontrado.")
"""



tiempo = timeit.timeit("buscar1(4554)", setup=codigo, number=1000) # La ejecuta 1000 veces

print(f"La función se ejecutó en promedio {tiempo/1000} segundos por ejecución.")