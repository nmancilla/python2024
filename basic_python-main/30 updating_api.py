import requests
import json


# 1. Obtenga toda la información de los usuarios retornada por la API, guárdela en una variable
# llamada users_data e imprímala en pantalla.

def request_get(url): 
    return json.loads(requests.get(url).text) 

url = "https://reqres.in/api/users"

users_data = request_get(url)

print(json.dumps(users_data, indent=4))









# 2. Cree un usuario que tenga de nombre Ignacio y de trabajo Profesor. Guarde el
# diccionario de respuesta en una variable llamada created_user e imprímala en pantalla.

nombre = 'Ignacio'
trabajo = 'Profesor'

new_user = {
    "nombre": f"{nombre}",
    "trabajo": f"{trabajo}"
}

data = json.dumps(new_user)
created_user = requests.post(url, data)
print(created_user)
print(created_user.text)








# 3. Actualice un usuario llamado morpheus para que tenga un campo llamado residence  igual a zion. 
# Guarde el diccionario de respuesta en una variable llamada updated_user e imprímala en pantalla.

new_name = {
    "first_name": "Morpheus",
    "residence": "Zion"
}

data = json.dumps(new_name)
updated_user = requests.post('https://reqres.in/api/users/5', data)
print(updated_user)
print(updated_user.text)









# 4. Elimine un usuario llamado Tracey. Imprima el código de respuesta en pantalla.

response = requests.delete('https://reqres.in/api/users/6')
print(response)
print(response.text)

# Verifica la respuesta
if response.status_code == 204:
    print(f'Usuario eliminado correctamente.')
else:
    print(f'Error al eliminar el usuario. Código de estado: {response.status_code}')