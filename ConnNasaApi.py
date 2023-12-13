# Archivo que contiene las funciones para conectarse a la API de la NASA

# Importamos el modulo requests
import requests


# función para obtener los datos del recurso A.P.O.D(astronomic picture of the day)
def obtener_datos_apod(api_key):
    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al conectarse a la API de la NASA")
        return None


# función para obtener los datos de la foto del día según una fecha específica
def obtener_foto_del_dia_segun_fecha(api_key, fecha):
    url = "https://api.nasa.gov/planetary/apod"
    
    # Parámetros de la API, incluyendo la clave de la API y la fecha deseada
    params = {
        "api_key": api_key,
        "date": fecha
    }

    # Realizar la solicitud GET a la API
    response = requests.get(url, params=params)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener los datos de la respuesta en formato JSON
        data = response.json()
        
        # Verificar si se obtuvieron los datos correctamente
        if 'title' in data and 'hdurl' in data and 'explanation' in data:
            return data
        else:
            print("Los datos de la respuesta no contienen la información esperada.")
            return None
    else:
        # Mostrar un mensaje de error si la solicitud falló
        print(f"Error al conectarse a la API de la NASA. Código de estado: {response.status_code}")
        return None
    

# función para obtener datos de asteroides cercanos a la Tierra
def obtener_asteroides_cercanos(api_key, fecha):
    url = "https://api.nasa.gov/neo/rest/v1/feed"

    # Parámetros de la API, incluyendo la clave de la API y la fecha deseada
    params = {
        "api_key": api_key,
        "start_date": fecha,
        "end_date": fecha
    }

    # Realizar la solicitud GET a la API
    response = requests.get(url, params=params)
    print(response)

    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener los datos de la respuesta en formato JSON
        data = response.json()
        
        print(data)
        # Verificar si se obtuvieron los datos correctamente
        if 'title' in data or 'image' in data or 'explanation' in data:
            return data
        else:
            print("Los datos de la respuesta no contienen la información esperada.")
            return None
    else:
        # Mostrar un mensaje de error si la solicitud falló
        print(f"Error al conectarse a la API de la NASA. Código de estado: {response.status_code}")
        return None



