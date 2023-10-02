import requests 
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


url = "https://www.cuspide.com"

topPath = url + "/100-mas-vendidos"

urlDolar = "https://dolarhoy.com/cotizaciondolarblue"
# Para que simule ser navegador web
# parece a la información que un navegador Chrome real
# enviaría en su solicitud HTTP

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

def get_request(url, headers): 
    try: 
        response = requests.get(url, headers = headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except requests.exceptions.RequestException as req_err:
        print(f"Error en la solicitud: {req_err}")
        return None

result = get_request(topPath, headers)

soup = BeautifulSoup(result, 'html.parser')

resultDolar = get_request(urlDolar, headers)

soupDolar = BeautifulSoup(resultDolar, 'html.parser')
venta_Dolar = (soupDolar.find("div", class_="topic", text = "Venta")).find_next().getText()
character = "$"
venta_Dolar = float((venta_Dolar.replace(character, "")))

print(venta_Dolar)

# Encontrar todas las etiquetas 'a' con el atributo 'href'
elements_html = soup.find_all("div", class_ = "box-image-top")

href_element = []
title_element = []
priceArg_element = []
priceDolar_element = []

elements_books = []

for div_element in elements_html:
    a_elements = div_element.find_all("a", href=True)

    for a_element in a_elements:
        href_element.append(a_element["href"])

for element in href_element:
    res = get_request(element, headers)
    soup2 = BeautifulSoup(res,'html.parser')
    title_element = (soup2.find("h1", class_ = "product-title product_title entry-title").getText().replace("\n", "").replace("\t", ""))
    
    urlbook = element
    # Buscar el fragmento JSON-LD en el código HTML
    script_tag = soup2.find('script', type='application/ld+json')
    json_ld = script_tag.string
    # Analizar el contenido JSON-LD
    data = json.loads(json_ld)

    # Acceder al precio
    priceArg_element = (data['@graph'][1]['offers'][0]['price'])
    priceArg_element = float(priceArg_element)
    priceDolar_element = (soup2.find("span", style= "font-size: 1.3em").getText())
    priceDolar_element = float(priceDolar_element.replace(",","."))
    time = datetime.now()
    format_time = time.strftime("%Y-%m-%d")

    
    book_dict = {
        "title" : title_element,
        "url" : urlbook,
        "priceArg" : priceArg_element,
        "priceDolar" : priceDolar_element,
        "priceDolarBlue" : round((priceArg_element/venta_Dolar),2),
        "date" : format_time
    }


    elements_books.append(book_dict)
    print(elements_books)




