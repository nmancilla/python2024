import requests
import json

# Solicito las imágenes
url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)

# Transformo el resultado 
photos = json.loads(response.text)

# Acortamos
photos = photos[0:8]


# Armamos el texto que contiene todas las cols
cols_3 = ''
for photo in photos:
    cols_3 += f'''<div class="col-3">
                    <div class="card">
                        <img src="{photo['url']}" alt="">
                        <h4>{photo['title']}</h4>
                    </div>
                </div'''


# Armamos el html completo
html_template = f'''<!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bootstrap demo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body>
        <h1>Blog Simple</h1>
        <div class="container">
            <div class="row">
                {cols_3}
            </div>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
</html>
'''

# Crear un archivo html y agrgar texto completo
with open('index.html', 'w') as f:
    f.write(html_template)


# Ejecutar chomre a pantalla completa con el archivo creado
