from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from flask import Flask, jsonify
import os

app = Flask(__name__)

def scrape_currencies():
    # Algunas configuraciones de Firefox para que no se abra la ventana
    options = Options()
    options.add_argument('--headless') 
    options.add_argument('--disable-gpu')  
    options.add_argument('--no-sandbox') 

    # Ruta al geckodriver en la misma carpeta del proyecto
    geckodriver_path = os.path.join(os.getcwd(), 'geckodriver')

    # Inicializa el servicio para el WebDriver de Firefox
    service = Service(geckodriver_path)

    # Inicializa el WebDriver de Firefox con el servicio configurado
    driver = webdriver.Firefox(service=service, options=options)

    try:
        url = "https://www.brou.com.uy/cotizaciones"
        driver.get(url)

        # Encuentra la tabla de cotizaciones usando XPath o CSS Selectors
        table = driver.find_element("xpath", '//table')

        # Extrae las filas de la tabla
        rows = table.find_elements("xpath", './/tr')[1:]  # Ignora el encabezado

        currencies = []
        for row in rows:
            columns = row.find_elements("xpath", './/td')
            if len(columns) > 0:
                currency_name = columns[0].find_element("class name", 'moneda').text.strip()
                compra = columns[2].find_element("class name", 'valor').text.strip()
                venta = columns[4].find_element("class name", 'valor').text.strip()

                currencies.append({
                    'moneda': currency_name,
                    'compra': compra,
                    'venta': venta
                })

    finally:
        driver.quit() # Acá cerramos el navegador

    return currencies

@app.route('/currencies', methods=['GET']) # Levanto el Server
def get_currencies():
    currencies = scrape_currencies()
    if currencies:
        return jsonify(currencies)
    else:
        return jsonify({"error": "No se pudieron obtener las cotizaciones"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
