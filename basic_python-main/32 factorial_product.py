velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

def mediciones(velocidad):
    totales = 0
    for valores in velocidad:
        totales += valores
    promedio = totales / len(velocidad)
    posiciones = []
    for pos, val in enumerate(velocidad):
        if val > promedio:
            posiciones.append(pos)
    print(posiciones)



def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def productoria(lista_valores):
    producto = 1
    for i in lista_valores:
        producto *= i
    return producto

def calcular(fact_1, prod_1, fact_2):
    resultado_factorial1 = factorial(fact_1)
    resultado_productoria = productoria(prod_1)
    resultado_factorial2 = factorial(fact_2)
    print(f'El factorial de {fact_1} es {resultado_factorial1}')
    print(f'La productoria de {prod_1} es {resultado_productoria}')
    print(f'El factorial de {fact_2} es {resultado_factorial2}')


if __name__ == '__main__': #Solo se ejecuta cuando el archivo se ejecuta directamente
    calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)
    mediciones(velocidad)