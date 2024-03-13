import requests

# URL de la API de tarjetas de crédito
url = 'https://fakerapi.it/api/v1/credit_cards?_quantity=1'

try:
    # Realiza la solicitud GET a la API
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convierte la respuesta a formato JSON
        credit_card_data = response.json()

        # Extrae la información de la tarjeta de crédito
        card_info = credit_card_data['data'][0]

        # Muestra la información de la tarjeta de crédito
        print("Información de la tarjeta de crédito:")
        print(f"Tipo: {card_info['type']}")
        print(f"Número: {card_info['number']}")
        print(f"Fecha de vencimiento: {card_info['expiration']}")
        print(f"Propietario: {card_info['owner']}")
    else:
        print(f"Error al consumir la API. Código de estado: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")
