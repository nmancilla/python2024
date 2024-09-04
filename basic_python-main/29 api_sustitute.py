import requests
import json
from string import Template

def request_get(url):
    return json.loads(requests.get(url).text) 


out = request_get('https://jsonplaceholder.typicode.com/photos')[:5] #solo 5
print((out)) #5000 (fotos)

print(out[0].keys()) #Para ver solo las llaves/claves del primer elemento

print(out[0]) # Muesta todas las llave y valores de cada diccionario




img_template = Template('<img src="$urle">') # Se crea un template

# imagen = img_template.substitute(url = 'hola') #Se sustituye el template
# print(imagen)





html_template = Template('''
<!DOCTYPE html>
<html>
<head>
<title>Título de la Página</title>
</head>
<body>
<h1>Nuestra página Web</h1>
$body
</body>
</html>
''')




lista_url = [elemento['url'] for elemento in out]
texto_img = ''
for url in lista_url:
    texto_img += img_template.substitute(urle = url)+'\n'

print(texto_img)


final = html_template.substitute(body = texto_img)
print(final)






