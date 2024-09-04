import sys
def mayor_a():
    ventas = {
        "Enero": 15000,
        "Febrero": 22000,
        "Marzo": 12000,
        "Abril": 17000,
        "Mayo": 81000,
        "Junio": 13000,
        "Julio": 21000,
        "Agosto": 41200,
        "Septiembre": 25000,
        "Octubre": 21500,
        "Noviembre": 91000,
        "Diciembre": 21000,
    } 
    cantidad = int(sys.argv[1]) #para recibir el argumento desde la terminal 
    filtradas = {llave: valor for llave, valor in ventas.items() if valor > cantidad}
    print(filtradas)
mayor_a()
