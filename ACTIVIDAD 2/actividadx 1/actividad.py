import requests
from bs4 import BeautifulSoup
import json

url = 'https://pueblosoriginarios.com/lenguas/mayas.php'

response = requests.get(url)

if response.status_code == 200:

  soup = BeautifulSoup(response.text,'html.parser')

  table = soup.find('table',{'id':'diccionario'})

  rows = table.find_all('tr')

  diccionario_data = []

  for row in rows[1:]:
    cols = row.find_all('td')

    if len(cols) == 2:
      maya_word = cols[0].text.strip()
      spanish_word = cols[1].text.strip()
      diccionario_data.append({'Maya':maya_word, 'Español':spanish_word})

  json_data = json.dumps(diccionario_data, indent=4, ensure_ascii=False)

  with open('diccionario_maya.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

  print("Datos extraidos y guardados en diccionario_maya.json")  

else:

  print("error al conectarse a la web") 
    