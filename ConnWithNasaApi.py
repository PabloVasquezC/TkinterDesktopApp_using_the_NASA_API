import requests

# URL de la API de la NASA
url = "https://api.nasa.gov/planetary/apod"

# Parámetros de la API (en este caso, la clave de API)
params = {
    "api_key": "HLFsRfhi3gr2qxHdowAo6rjIr3xjUHtCdtcaDCk6"
}

# Realizar la solicitud GET a la API
response = requests.get(url, params=params)

# Comprobar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener los datos de la respuesta en formato JSON
    data = response.json()
    print(f"Título: {data['title']}")
    print(f"Autor: {data['copyright']}")
    print(f"Fecha: {data['date']}")
    print(f"Imagen: {data['url']}")
    print(f"Descripción: {data['explanation']}")
else:
    # Mostrar un mensaje de error si la solicitud falló
    print("Error al conectarse a la API de la NASA")
