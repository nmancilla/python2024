import random

# Generar un número aleatorio entre 0 y 1
numero_aleatorio = random.random()
print(numero_aleatorio)

# Generar un número entero aleatorio dentro de un rango
numero_entero = random.randint(1, 10)
print(numero_entero)

# Elegir un elemento aleatorio de una lista
lista = ['manzana', 'banana', 'cereza']
elemento_aleatorio = random.choice(lista)
print(elemento_aleatorio)


# random.randrange() devuelve un elemento de rango(start, stop, step)
numero_rango = random.randrange(0, 101, 10)  # Número aleatorio entre 0 y 100, múltiplo de 10
print(numero_rango)

# random.uniform() devuelve un número flotante aleatorio entre los valores dados
numero_flotante = random.uniform(1.5, 1.9)  # Número flotante aleatorio entre 1.5 y 1.9
print(numero_flotante)


# random.shuffle() mezcla los elementos de una lista en el lugar
lista_numeros = [1, 2, 3, 4, 5]
random.shuffle(lista_numeros)  # Mezcla la lista de números
print(lista_numeros)
