import requests

# URL de la API de direcciones
url = 'https://fakerapi.it/api/v1/addresses?_quantity=1'

try:
    # Realiza la solicitud GET a la API
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convierte la respuesta a formato JSON
        address_data = response.json()

        # Extrae la información de la dirección
        address_info = address_data['data'][0]
        
        # Muestra la información de la dirección
        print("Información de la dirección:")
        print(f"Calle: {address_info['street']}")
        print(f"Nombre de la calle: {address_info['streetName']}")
        print(f"Número de edificio: {address_info['buildingNumber']}")
        print(f"Ciudad: {address_info['city']}")
        print(f"Código postal: {address_info['zipcode']}")
        print(f"País: {address_info['country']}")
        print(f"Código de condado: {address_info['county_code']}")
        print(f"Latitud: {address_info['latitude']}")
        print(f"Longitud: {address_info['longitude']}")
    else:
        print(f"Error al consumir la API. Código de estado: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")
