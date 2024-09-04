# JSON : JavaScript Object Notation
# curl hace solicitudes a una api dese el terminal
# Otra forma es la web Yarc
# Es por Python


# 200 OK: La solicitud ha tenido éxito.
# 201 Created: Se ha creado un nuevo recurso como resultado de la solicitud (por ejemplo, después de una petición PUT).
# 204 No Content: La solicitud se ha completado con éxito, pero la respuesta no tiene contenido (aunque los encabezados pueden ser útiles).
# 400 Bad Request: La solicitud contiene una sintaxis no válida o el servidor no puede cumplirla.
# 401 Unauthorized: El cliente debe proporcionar credenciales de autenticación.
# 404 Not Found: El recurso solicitado no existe en el servidor.
# 500 Internal Server Error: Hubo un error interno en el servidor


# json.loads  para trasnformar de JSON (texto) a un diccionario de Python
# json.dumps  para transformar desde un diccionario Python a JSON (texto)



import requests
import json
import pdb



# # Consulta básica
# url = 'https://reqres.in/api/users'
# response = requests.get(url)
# users_data = json.loads(response.text) # Tranforma en diccionario para iterar
# print(users_data)
# print(type(users_data))







# import requests
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# print(response) # Muestra el tipo de mansaje
# print(response.text) # Muestra iun string







# url = 'https://anapioficeandfire.com/api/characters/583'
# response = requests.get(url)
# # print(response.text) # Imprime solo texto, ya que llega como texto
# jon_snow = json.loads(response.text) # Lo transforma en un diccionario
# print('Estos son los apodos de Jon Snow:')
# for apodo in jon_snow['aliases']:
#     print(apodo)







# #Requerimiento simple
# def request_get(url): 
#     return json.loads(requests.get(url).text) 

# url = 'https://reqres.in/api/users'

# users_data = request_get(url)
# print(json.dumps(users_data, indent=4))










# #Posteo
# url = 'https://jsonplaceholder.typicode.com/posts'
# data = {
#     'userID': 1,
#     'title': 'hola',
#     'body': 'Este es mi primer posteo desde Python'
# }
# data = json.dumps(data)
# headers = {
#     'Content-Type': 'application/json'
# }

# response = requests.post(url, headers, data) #Envía la información, post
# print(response)
# print(response.text)
# #pdb.set_trace() #response.status_code // response.text
# #breakpoint() #Tambien se puede usar









# def probar_put():
#     url = 'https://jsonplaceholder.typicode.com/posts/20' #Debe incluir la ID
#     data = {
#         'userId': 2,
#         'title': 'Articulo Modificador',
#         'body': 'Este es la corrección'
#     }
#     # data = json.dumps(data)
#     # requests.put(): Esta función acepta un argumento adicional llamado json, que te permite pasar 
#     # directamente un diccionario (o cualquier objeto serializable) como datos. Internamente, 
#     # requests se encargará de convertirlo a JSON antes de enviar la solicitud PUT.

#     response = requests.put(url, json=data) #Put acepta dos argumentos posicionales, no header
#     print(response.status_code)

# if __name__ == '__main__':
#     probar_put()











# import json
# import requests

# class Mindicador:
#     def __init__(self, indicador, year):
#         self.indicador = indicador
#         self.year = year

#     def InfoApi(self):
#         # En este caso hacemos la solicitud para el caso de consulta de un indicador en un año determinado
#         url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
#         response = requests.get(url)
#         data = json.loads(response.text.encode("utf-8"))
#         # Para que el json se vea ordenado, retornar pretty_json
#         pretty_json = json.dumps(data, indent=2)
#         return data

# indicador = input('Qué dato desea consultar (bitcoin, uf, dolar, utm):\n')
# fecha = input('Indique la fecha en el siguiente formato dd-mm-aaaa:\n')
# respuesta = Mindicador(indicador, fecha)
# datos = respuesta.InfoApi()
# print(f"Nombre del indicador: {datos['nombre']}")
# print(f"Valor: {datos['serie'][0]['valor']}")







# import requests
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# datos = json.loads(response.text)

# print(datos[0]) # Muestra el primer resultado
# print(datos[0].keys()) # Muestra las llaves/claves del primer resultado
# print(datos[0]['title']) # Muestra el valor de la llave title

# #mostrar todos los títulos en lista
# titulos = [post['title'] for post in datos]
# print(type(titulos))



# # Cierta cantindad de datos
# import requests
# def request_get(url):
#     response = json.loads(requests.get(url).text)
#     return response

# solicitud = request_get('https://jsonplaceholder.typicode.com/posts')[3:6] #elementos pos 3 al 6
# print(solicitud)








# # Post
# payload = '''{
#     "title": "Nuevo Post",
#     body": "Este es el contenido"
# }'''

# response = requests.post('https://jsonplaceholder.typicode.com/posts', data = payload)
# print(f'Este es el mensaje del servidor: {response}')
# print(response.text) 









# #Cambio o put. Se debe usar la ID
# payload = '''{
#     "tile": "Cambio de título,
#     "body": "Cuerpo de post",
#     "userID": 1    
# }'''

# response = requests.put('https://jsonplaceholder.typicode.com/posts/20', data = payload)
# print(f'Este es el mensaje del servidor: {response}')
# print(response.text) 







# #Autenficiación
# import json
# import requests

# app_id = ""
# app_key = ""

# word = "hello"

# url = f"https://od-api.oxforddictionaries.com/api/v2/entries/en/{word}"

# r = json.loads(requests.get(url, headers = {"app_id": app_id, "app_key": app_key}).text)
# print(r)
# print(r.keys())










import requests
import json


#Requerimiento simple
def request_get(url): 
    return json.loads(requests.get(url).text) 

url = 'https://reqres.in/api/users'

users_data = request_get(url)


print('\n*** Consultor de base de datos ***\n')
print('''¿Qué dato tiene para consultar?
1) Por ID
2) Por email''')
opcion = int(input('> '))

def consulta_id():
    id = int(input('Ingrese el ID para consular datos: ')) 
    for user in users_data['data']:
        if user['id'] == id:
            menu(user)  

def consulta_email():
    email = input('Ingrese el email para consular datos: ')
    for user in users_data['data']:
        if user['email'] == email:
            menu(user)

def menu(user):
    id = user['id']
    email = user['email']
    nombre = user['first_name']
    apellido = user['last_name']
    print(f'El nombre es: {nombre}\nEl apellido es: {apellido}\nEl email es: {email}\nEl ID es: {id} ')

if opcion == 1:
    consulta_id()
elif opcion == 2:
    consulta_email()