def adornar(mensaje = 'Sin mensaje', adorno = '\u2728'): 
    return f'{adorno} {mensaje} {adorno}'

texto = adornar(adornar(adornar('Hola'))) 
print(texto)

#Composición de funciones
def componer(func, mensaje, veces = 5):
    valor = mensaje
    for i in range(veces):
        valor = func(valor)
    return valor

print(componer(adornar, 'adios', 7))
