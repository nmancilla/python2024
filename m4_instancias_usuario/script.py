from usuario import Usuario
import json

lista = []
archivo = 'usuarios.txt'

def crear_archivo(archivo:str):
    archivo_abierto = open(archivo, 'r')
    lineas = archivo_abierto.readlines()
    for linea in lineas:
        try:
            usuario = json.loads(linea)
        except Exception as e:
            with open('error.log', 'a') as log:
                log.write(f'Hubo un error: {e}\n')
        finally:
            # Tomaremos cada valor del usuario
            nombre = usuario.get('nombre')
            apellido = usuario.get('apellido')
            email = usuario.get('email')
            genero = usuario.get('genero')
            # Creamos una instancia de usuario
            nuevo_usuario = Usuario(nombre, apellido, email, genero)
            # Agregamos ese usuario a la lista
            lista.append(nuevo_usuario)
    print(lista)

if __name__ == '__main__':
    crear_archivo('usuarios.txt')