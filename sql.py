import pymysql
import preproyecto_web_scrapping as scrap

elementsList = scrap.elements_books
 
#Conexión con bbdd

host = 'localhost'
user = 'root'
password = ''


conn = pymysql.connect(host=host, user=user, password=password)

# Crear un cursor para ejecutar comandos SQL

try:
    cursor = conn.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS books')
    conn.select_db('books')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weekly_top_100(
            id INT AUTO_INCREMENT PRIMARY KEY, 
            title VARCHAR (100) NOT NULL, 
            url VARCHAR(250)  NOT NULL, 
            price DECIMAL(10,2), 
            price_usd DECIMAL(10,2), 
            price_usd_blue DECIMAL(10,2), 
            upload_date DATE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS error(
            id INT AUTO_INCREMENT PRIMARY KEY, 
            title VARCHAR (100) NOT NULL, 
            url VARCHAR(250)  NOT NULL, 
            upload_date DATE NOT NULL
        ) 
    ''')

    print("Se creo la tabla")

except Exception as e:
    print("No se pudo crear la base de datos y la tabla:", str(e))

# Verificar si el título o la URL son vacíos o nulos
for datos in elementsList:
    if datos['title'] is not None or datos['title'] != '' or datos['url'] is not None or datos['url'] != '':
        sql_main_table = "INSERT INTO weekly_top_100 (title, url, price, price_usd, price_usd_blue, upload_date) VALUES (%s, %s, %s, %s, %s, %s)"
        
        try:
            cursor.execute(sql_main_table, (datos['title'], datos['url'], datos['priceArg'], datos['priceDolar'], datos['priceDolarBlue'], datos['date']))
            conn.commit()
            print("Los datos se han insertado correctamente en la tabla principal.")
        except Exception as e:
            conn.rollback()
            print("No se pudo insertar los datos en la tabla principal:", str(e))

        
    else:
        # Si el título o la URL son vacíos o nulos, inserta los datos en la tabla de errores
        sql_error = "INSERT INTO error (title, url, price, price_usd, price_usd_blue, upload_date) VALUES (%s, %s, %s, %s, %s, %s)"
        
        try:
            cursor.execute(sql_error, (datos['title'], datos['url'], datos['priceArg'], datos['priceDolar'], datos['priceDolarBlue'], datos['date']))
            conn.commit()
            print("Los datos se han insertado en la tabla de errores debido a título o URL vacíos o nulos.")
        except Exception as e:
            conn.rollback()
            print("No se pudo insertar los datos en la tabla de errores:", str(e))

# Cierra el cursor y la conexión
cursor.close()
conn.close()
