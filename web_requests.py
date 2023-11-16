import requests

def get_request(url, headers): 
    """
    Realiza una solicitud GET a la URL proporcionada con los headers dados.

    Args:
    - url (str): URL a la que se realiza la solicitud GET.
    - headers (dict): Headers para simular ser un navegador web.

    Returns:
    - str or None: Contenido de la respuesta de la solicitud GET o None si hay un error.
    """
    try: 
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
        return None
