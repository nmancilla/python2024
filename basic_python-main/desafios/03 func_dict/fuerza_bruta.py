import getpass
from string import ascii_lowercase

def passgord():
    password = getpass.getpass('Ingrese una contraseña: ')
    intento = 0
    for letra_pass in password:
        for letra_asci in ascii_lowercase:
            intento += 1
            if letra_asci == letra_pass:
                break
    print(f'La contraseña fue forzada en {intento} intentos')
passgord()