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

#CLASE DEL DIA 27 ENERO

  import pandas as pd

# Cargar los datos desde archivo json
with open('diccionario_maya.json','r', encoding='utf-8') as file:
  diccionario_data = json.load(file)

# Crear un dataframe
df = pd.DataFrame(diccionario_data)

# Crear el excel a partir del DataFrame
df.to_excel('diccionario_maya.xlsx', index=False)

print("Datos guardados en el diccionario_maya.xlsx")

import pandas as pd
import json

# Cargar los datos desde archivo json
with open('diccionario_maya.json','r', encoding='utf-8') as file:
  diccionario_data = json.load(file)

# Crear un dataframe
df = pd.DataFrame(diccionario_data)

# 1. Estadisticas descriptiva

descripcion_maya = df['Maya'].describe()
descripcion_espanol = df['Español'].describe()

print("Estadistica descriptiva de las palabras Maya")
print(descripcion_maya)

print("Estadistica descriptiva de las palabras Español")
print(descripcion_espanol)

#2. filtrar datos

palabras_con_a = df[df['Maya'].str.startswith('a',na=False)]

print("Palabras que comienzan con 'a' : ")
print(palabras_con_a)

#3. ordenar datos

df_ordenado = df.sort_values(by='Maya', key=lambda x: x.str.len(),ascending=True)

print("Palabras Ordenadas :")
print(df_ordenado)

#4. Contar duplicados

duplicados_maya = df[df.duplicated(subset='Maya', keep=False)]

print("Palabras Duplicadas en Maya")
print(duplicados_maya)

import mysql.connector
import json

#CONECTAR A LA BDATOS
conn = mysql.connector.connect(
    host="mysql-raulmtz.alwaysdata.net",
    user="raulmtz_us",
    password="Vingcard15",
    database="raulmtz_bd"
)

#VARIABLE DE CONSULTA A LA BASE DEDATOS
cursor = conn.cursor()

#CARGAR EL ARCHIVO JSON
with open ('diccionario_maya.json', 'r', encoding = 'utf-8') as file:
  diccionario_data = json.load(file)

  for palabra in diccionario_data:
    maya = palabra['Maya']
    espanol = palabra['Español']
    insert_query = "INSERT INTO diccionario_json (maya,espanol)VALUES(%s,%s)"
    cursor.execute(insert_query,maya,espanol)

    conn.commit()
    cursor.close()
    conn.close()

#CARGAR EL ARCHIVO EN PANDAS

    import pandas as pd

    df_excel = pd.read_excel('diccionario_maya.xlsx')