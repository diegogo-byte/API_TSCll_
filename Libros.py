import requests

# URL de la API de libros
url = 'https://fakerapi.it/api/v1/books?_quantity=1'

try:
    # Realiza la solicitud GET a la API
    response = requests.get(url)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convierte la respuesta a formato JSON
        book_data = response.json()

        # Muestra los datos del libro
        print("Datos del libro:")
        print(f"Título: {book_data['data'][0]['title']}")
        print(f"Autor: {book_data['data'][0]['author']}")
        print(f"Género: {book_data['data'][0]['genre']}")
        print(f"Año de publicación: {book_data['data'][0]['published']}")
    else:
        print(f"Error al consumir la API. Código de estado: {response.status_code}")

except Exception as e:
    print(f"Error: {e}")
