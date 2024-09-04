import sys, math

def num_palabra(num):
  primeros15 = ['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis', 'siete', 'ocho', 'nueve', 'diez', 'once', 'doce', 'trece', 'cartorce', 'quince']

  if num <= 15:
    return primeros15[num]
  # dieci-algo
  elif num <= 19:
    unidades = num - 10
    return 'dieci' + num_palabra(unidades)
  # veinte
  elif num == 20:
    return 'veinte'
  # veinti-algo
  elif num <= 29:
    unidades = num - 20
    return 'veinti' + num_palabra(unidades)
  # algo y algo
  elif num <= 99:
    decenas = math.floor(num / 10)
    unidades = num - (decenas * 10)
    decenas_palabras = ['', '', '', 'treinta', 'cuarenta', 'cincuenta', 'sesenta', 'setenta', 'ochencha', 'noventa']
    if unidades == 0:
      return decenas_palabras[decenas]
    return decenas_palabras[decenas] + ' y ' + num_palabra(unidades)
  elif num == 100:
    return 'cien'
  # ciento y algo
  elif num <= 199:
    resto = num - 100
    return 'ciento ' + num_palabra(resto)
  
  elif num <= 999:
    centenas_palabras = ['', '', 'doscientos', 'trescientos', 'cuatrocientos', 'quinientos', 'seisientos', 'setecientos', 'ochocientos', 'novecientos']
    centenas = math.floor( num / 100) #Función piso. Elimina los decimales
    resto = num - (centenas * 100)
    if resto == 0:
      return centenas_palabras[centenas]
    return centenas_palabras[centenas] + ' ' + num_palabra(resto)
  
  elif num == 1000:
    return 'luca'
  elif num <= 1999:
    resto = num - 1000
    return 'mil ' + num_palabra(resto)
  elif num <= 999999:
    miles = math.floor(num / 1000)
    resto = num - (miles * 1000)
    if resto == 0:
      return num_palabra(miles) + ' mil'
    return num_palabra(miles) + ' mil ' + num_palabra(resto)
  elif num == 1_000_000:
    return 'un millón'
  elif num <= 1_999_999:
    resto = num - 1_000_000
    return 'un millon ' + num_palabra(resto) 
  elif num <= 1_000_000_000_000:
    millones = math.floor(num / 1_000_000)
    resto = num - (millones * 1_000_000)
    return num_palabra(millones) + ' millones' +  num_palabra(resto)
  else:
    return 'no implementado'

print(num_palabra(int(sys.argv[1])))