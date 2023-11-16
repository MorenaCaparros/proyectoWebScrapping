import requests 
from bs4 import BeautifulSoup
import json
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

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
        response = requests.get(url, headers = headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
        return None


def extract_books_info(soup, dollar_value):
    elements_books = []

    elements_html = soup.find_all("div", class_="box-image-top")

    for div_element in elements_html:
        a_elements = div_element.find_all("a", href=True)
        for a_element in a_elements:
            href = a_element["href"]

            res = get_request(href, headers)  # Usar tu función get_request aquí
            soup2 = BeautifulSoup(res, 'html.parser')

            title_element = soup2.find("h1", class_="product-title product_title entry-title").getText().replace("\n", "").replace("\t", "")

            script_tag = soup2.find('script', type='application/ld+json')
            json_ld = script_tag.string
            data = json.loads(json_ld)
            priceArg_element = float(data['@graph'][1]['offers'][0]['price'])

            container_element = soup2.find("div", class_="row content-row mb-0")
            if container_element:
                priceDolar_element = container_element.find("span", style="color: #111; font-weight: 400; font-size: 1.1em")
                if priceDolar_element:
                    next_element = priceDolar_element.find_next("span", style="font-size: 1.3em")
                    if next_element:
                        valor_dolar = next_element.get_text(strip=True).replace(",", ".")
                        priceDolar_element = float(valor_dolar)
                    else:
                        priceDolar_element = 0.0
                else:
                    if container_element.find("p", class_="stock out-of-stock"):
                        priceDolar_element = 0.0
                    else:
                        priceDolar_element = 0.0

            time = datetime.now()
            format_time = time.strftime("%Y-%m-%d")

            book_dict = {
                "title": title_element,
                "url": href,
                "priceArg": priceArg_element,
                "priceDolar": priceDolar_element,
                "priceDolarBlue" : round((priceArg_element/dollar_value),2),
                "date": format_time
            }
            elements_books.append(book_dict)

    return elements_books

def extract_dollar_value(soupDolar):
    venta_Dolar = 0.0

    venta_Dolar_element = soupDolar.find("div", class_="topic", text="Venta").find_next().getText()
    character = "$"
    venta_Dolar = float(venta_Dolar_element.replace(character, ""))

    return venta_Dolar
