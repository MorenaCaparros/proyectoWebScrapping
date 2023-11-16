from bs4 import BeautifulSoup
from data_extraction import extract_books_info, extract_dollar_value
from web_requests import get_request
from database_operations import create_database_tables, insert_data_to_db

url = "https://www.cuspide.com"
topPath = url + "/100-mas-vendidos"
urlDolar = "https://dolarhoy.com/cotizaciondolarblue"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# Obtener contenido de la página de libros más vendidos
result = get_request(topPath, headers)
soup = BeautifulSoup(result, 'html.parser')

# Obtener contenido de la página de cotización del dólar
resultDolar = get_request(urlDolar, headers)
soupDolar = BeautifulSoup(resultDolar, 'html.parser')

# Crear las tablas en la base de datos (si aún no existen)
create_database_tables()

# Extraer información de libros y valor del dólar
dollar_value = extract_dollar_value(soupDolar)
books_info = extract_books_info(soup, dollar_value)

# Insertar los datos en la base de datos
insert_data_to_db(books_info)
