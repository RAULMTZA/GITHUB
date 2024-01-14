import requests
from bs4 import BeautifulSoup
import json
from openpyxl import Workbook

url = 'https://pueblosoriginarios.com/lenguas/mayas.php'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'diccionario'})

    rows = table.find_all('tr')

    diccionario_data = []

    for row in rows[1:]:
        cols = row.find_all('td')

        if len(cols) == 2:
            maya_word = cols[0].text.strip()
            spanish_word = cols[1].text.strip()
            diccionario_data.append({'Maya': maya_word, 'Español': spanish_word})

    # Crear un nuevo libro de Excel y seleccionar la hoja activa
    workbook = Workbook()
    sheet = workbook.active

    # Agregar encabezados
    sheet['A1'] = 'Maya'
    sheet['B1'] = 'Español'

    # Rellenar datos
    for idx, data in enumerate(diccionario_data, start=2):
        sheet[f'A{idx}'] = data['Maya']
        sheet[f'B{idx}'] = data['Español']

    # Guardar el libro de Excel
    workbook.save('diccionario_maya.xlsx')

    print("Datos extraídos y guardados en diccionario_maya.xlsx")

else:
    print("error al conectarse a la web")
