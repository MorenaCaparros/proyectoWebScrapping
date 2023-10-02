# proyectoWebScrapping
Proyecto para soyHenry de Web Scrapping

# Proyecto de Web Scraping para Libros - README

Este proyecto de Web Scraping se enfoca en recopilar información sobre los libros más vendidos en una tienda en línea y almacenarla en una base de datos MySQL. El proyecto consta de dos archivos principales: `preproyecto_web_scrapping.py` y `sql.py`.

## Resumen del Proyecto

El proyecto se divide en dos partes principales:

### Parte 1: Web Scraping

El archivo `preproyecto_web_scrapping.py` realiza la extracción de datos desde el sitio web de Cúspide, específicamente la sección de los 100 libros más vendidos. Utiliza las siguientes bibliotecas:

- `requests` para realizar solicitudes HTTP al sitio web.
- `BeautifulSoup` para analizar el contenido HTML.
- `json` para procesar datos en formato JSON.
- `datetime` para registrar la fecha y hora de la extracción.

El proceso incluye lo siguiente:

- Se obtiene la cotización del dólar blue desde el sitio "DolarHoy".
- Se extrae información sobre los libros más vendidos, incluyendo título, URL, precio en pesos argentinos y precio en dólares.
- Se calcula el precio en dólares blue utilizando la cotización previamente obtenida.
- Los datos se almacenan en una lista de diccionarios.

### Parte 2: Base de Datos

El archivo `sql.py` se encarga de la conexión a una base de datos MySQL y el almacenamiento de los datos extraídos. Utiliza la biblioteca `pymysql` para interactuar con la base de datos. El proceso incluye lo siguiente:

- Se crea una base de datos llamada "books" si no existe.
- Se crea una tabla llamada "weekly_top_100" para almacenar los datos de los libros.
- Se crea una tabla llamada "error" para almacenar los datos de libros con información faltante.
- Se insertan los datos extraídos en la tabla principal o en la tabla de errores según el estado de la información.

## Requisitos

Asegúrate de tener instaladas las siguientes bibliotecas de Python:

- requests
- BeautifulSoup
- json
- pymysql

Además, se requiere un servidor MySQL local o remoto para almacenar los datos.

## Uso

1. Ejecuta `preproyecto_web_scrapping.py` para realizar la extracción de datos.
2. Ejecuta `sql.py` para almacenar los datos en la base de datos MySQL.

## Configuración de la Base de Datos

Asegúrate de configurar adecuadamente los detalles de la base de datos en el archivo `sql.py` antes de ejecutarlo. Puedes especificar la dirección del host, el usuario y la contraseña de MySQL.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir o mejorar este proyecto, no dudes en crear una solicitud de extracción.