# 30 Días de Python: Día 19 - Manejo de archivos

- [Día 19](#-día-19)
  - [Manejo de archivos](#manejo-de-archivos)
    - [Abrir un archivo para lectura](#abrir-un-archivo-para-lectura)
    - [Abrir un archivo para escritura y actualización](#abrir-un-archivo-para-escritura-y-actualización)
    - [Eliminar archivos](#eliminar-archivos)
  - [Tipos de archivos](#tipos-de-archivos)
    - [Archivos con extensión txt](#archivos-con-extensión-txt)
    - [Archivos con extensión json](#archivos-con-extensión-json)
    - [Convertir JSON a diccionario](#convertir-json-a-diccionario)
    - [Convertir diccionario a JSON](#convertir-diccionario-a-json)
    - [Guardar como archivo JSON](#guardar-como-archivo-json)
    - [Archivos con extensión csv](#archivos-con-extensión-csv)
    - [Archivos con extensión xlsx](#archivos-con-extensión-xlsx)
    - [Archivos con extensión xml](#archivos-con-extensión-xml)
  - [💻 Ejercicios: Día 19](#-ejercicios-día-19)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)
    - [Ejercicios: Nivel 3](#ejercicios-nivel-3)

# 📘 Día 19

## Manejo de archivos

Hasta ahora hemos visto distintos tipos de datos en Python. Normalmente almacenamos datos en distintos formatos de archivo. Además de manejar archivos, en esta sección veremos diferentes formatos (.txt, .json, .xml, .csv, .tsv, .excel). Primero, familiaricémonos con el manejo de archivos usando un formato común (.txt).

El manejo de archivos es una parte importante de la programación; nos permite crear, leer, actualizar y eliminar archivos. En Python usamos la función incorporada _open()_ para manipular archivos.

```py
# sintaxis
open('filename', mode) # mode(r, a, w, x, t, b) puede ser lectura, escritura o actualización
```

- "r" - lectura - valor por defecto. Abre el archivo solo para lectura; si no existe genera un error.
- "a" - append (añadir) - abre el archivo para agregar contenido al final; crea el archivo si no existe.
- "w" - escritura - abre el archivo para escribir, sobrescribe si existe; crea el archivo si no existe.
- "x" - crear - crea el archivo; si existe genera un error.
- "t" - texto - valor por defecto. Modo texto.
- "b" - binario - modo binario (por ejemplo para imágenes).

### Abrir un archivo para lectura

El modo por defecto de _open_ es lectura, así que no es necesario especificar 'r' o 'rt'. He creado un archivo llamado reading_file_example.txt en el directorio files. Veamos:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

Como en el ejemplo, al imprimir el objeto archivo obtenemos información sobre él. Un archivo abierto permite distintos métodos de lectura: _read()_, _readline_, _readlines_. Debemos cerrar el archivo con _close()_ cuando terminemos.

- _read()_: lee todo el texto como una cadena. Podemos limitar el número de caracteres pasando un entero a *read(number)*.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# salida
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

En lugar de imprimir todo el texto, podemos leer solamente los primeros 10 caracteres:

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# salida
<class 'str'>
This is an
```

- _readline()_: lee solo la primera línea

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# salida
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: lee todo el texto línea por línea y devuelve una lista de líneas

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# salida
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

Otra forma de obtener todas las líneas como lista es usar _splitlines()_:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# salida
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

Debemos cerrar los archivos después de abrirlos. Es fácil olvidarse; por eso existe la construcción _with_ que cierra automáticamente:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# salida
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Abrir un archivo para escritura y actualización

Para escribir en un archivo hay que pasar el modo a _open()_:

- "a" - append - añade al final; crea el archivo si no existe.
- "w" - write - sobrescribe el contenido; crea el archivo si no existe.

Añadamos texto al archivo que hemos estado leyendo:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('Este texto debe añadirse al final')
```

Si el archivo no existe, el siguiente ejemplo creará uno nuevo:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('Este texto será escrito en el nuevo archivo creado')
```

### Eliminar archivos

Como vimos anteriormente, podemos crear y eliminar directorios con el módulo _os_. Para eliminar archivos también usamos _os_.

```py
import os
os.remove('./files/example.txt')
```

Si el archivo no existe, remove lanzará un error, por lo que es mejor comprobar:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('El archivo no existe')
```

## Tipos de archivos

### Archivos con extensión txt

Los archivos _txt_ son un formato muy común; ya vimos su uso más arriba. Ahora pasemos a JSON.

### Archivos con extensión json

JSON significa JavaScript Object Notation. Es básicamente una representación en cadena de un objeto JavaScript o de un diccionario Python.

_Ejemplo:_

```py
# diccionario
person_dct= {
    "name":"Mark",
    "country":"Philippines",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}
# JSON: la forma en cadena del diccionario
person_json = "{'name': 'Mark', 'country': 'Philippines', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
# Usamos triple comillas para que sea multilínea y más legible
person_json = '''{
    "name":"Mark",
    "country":"Philippines",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}'''
```

### Convertir JSON a diccionario

Para convertir JSON a diccionario importamos el módulo json y usamos _loads_.

```py
import json
# JSON
person_json = '''{
    "name": "Mark",
    "country": "Philippines",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''
# Convertir la cadena JSON a diccionario
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```sh
# salida
<class 'dict'>
{'name': 'Mark', 'country': 'Philippines', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### Convertir diccionario a JSON

Para convertir un diccionario a JSON usamos _dumps_.

```py
import json
# diccionario en Python
person = {
    "name": "Mark",
    "country": "Philippines",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
# convertir diccionario a cadena JSON
person_json = json.dumps(person, indent=4) # indent puede ser 2, 4, 8; formatea la salida
print(type(person_json))
print(person_json)
```

```sh
# salida
<class 'str'>
{
    "name": "Mark",
    "country": "Philippines",
    "city": "Helsinki",
    "skills": [
        "JavaScript",
        "React",
        "Python"
    ]
}
```

### Guardar como archivo JSON

También podemos guardar los datos en un archivo JSON:

```py
import json
# diccionario en Python
person = {
    "name": "Mark",
    "country": "Philippines",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

En el ejemplo usamos encoding y ensure_ascii para manejar caracteres no ASCII. Ejemplo con caracteres no ASCII:

```py
import json
person = {
    "name": "Mark Firenze",
    "country": "Spain",
    "city": "Madrid",
    "skills": ["JavaScript", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

Leamos el archivo JSON que acabamos de crear:

```py
import json
with open('./files/json_example.json', 'r', encoding='utf-8') as f:
    person = json.load(f)
    print(person)
```

```sh
# salida
{'name': 'Mark Firenze', 'country': 'Spain', 'city': 'Madrid', 'skills': ['JavaScript', 'React', 'Python']}
```

### Archivos con extensión csv

CSV significa Comma Separated Values (valores separados por comas). Es un formato sencillo para datos tabulares (como hojas de cálculo o bases de datos) muy común en ciencia de datos.

_Ejemplo CSV:_

```csv
"name","country","city","skills"
"Mark","Finland","Helsinki","JavaScript"
```

Ejemplo de lectura:

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w+ crea el archivo si no existe
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Encabezados: {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} viene de {row[1]}, {row[2]}. Conoce {row[3]}')
            line_count += 1
    print(f'Procesadas {line_count} líneas.')
```

```sh
# salida:
Encabezados: name, country, city, skills
Asabeneh viene de Finland, Helsinki. Conoce JavaScript
Procesadas 2 líneas.
```

También podemos escribir CSV:

```py
import csv
with open('./files/csv_example.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # escribir encabezados
    writer.writerow(['name', 'country', 'city', 'skills'])
    # escribir datos
    writer.writerow(['Mark', 'Finland', 'Helsinki', 'JavaScript'])
```

### Archivos con extensión xlsx

Para leer archivos Excel necesitamos instalar la librería xlrd (u otras alternativas). Ejemplo:

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### Archivos con extensión xml

XML es un lenguaje de marcado similar a HTML. Permite etiquetas personalizadas y se usa para datos estructurados. En Python hay varias librerías; aquí usamos xml.etree.ElementTree.

_Ejemplo XML:_

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScript</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

Usamos xml.etree.ElementTree para parsear:

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Etiqueta raíz:', root.tag)
print('Atributos:', root.attrib)
for child in root:
    print('Campo: ', child.tag)
```

```sh
# salida
Etiqueta raíz: person
Atributos: {'gender': 'female'}
Campo:  name
Campo:  country
Campo:  city
Campo:  skills
```

Obtener más detalles:

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Etiqueta raíz:', root.tag)
print('Atributos:', root.attrib)
for child in root:
    print('Campo: ', child.tag)
    if child.tag != 'skills':
        print(child.text)
    else:
        for skill in child:
            print(skill.text)
```

```sh
# salida
Etiqueta raíz: person
Atributos: {'gender': 'female'}
field:  name
Asabeneh
field:  country
Finland
field:  city
Helsinki
field:  skills
JavaScript
React
Python
```

## 💻 Ejercicios: Día 19

### Ejercicios: Nivel 1

1. Escribe una función que reciba un parámetro (nombre de archivo) y cuente el número de palabras del archivo.
2. Lee el archivo obama_speech.txt y cuenta las palabras.
3. Lee michelle_obama_speech.txt y cuenta las palabras.
4. Lee donald_speech.txt y cuenta las palabras.
5. Lee melina_trump_speech.txt y cuenta las palabras.

### Ejercicios: Nivel 2

1. Extrae todos los archivos Python del directorio del curso:
   a) Recorre la carpeta 30DaysOfPython, extrae todos los archivos .py y guarda sus nombres en files_list.txt
   b) Crea un script llamado find_python.py que pueda ejecutarse desde la línea de comandos
   c) Añade una opción --version para manejar argumentos de línea de comandos

### Ejercicios: Nivel 3

1. Crea un archivo JSON a partir del siguiente dataset:
    ```py
    python_libraries = [
    {
        "nombre_librería": "Django",
        "creador": "Adrian Holovaty",
        "primer_año_lanzamiento": 2005,
        "versión": "4.0.2",
        "uso": "Desarrollo web",
        "descripción": "Django permite construir aplicaciones web mejores y más rápido."
    },
    {
        "nombre_librería": "Flask",
        "creador": "Armin Ronacher",
        "primer_año_lanzamiento": 2010,
        "versión": "2.0.2",
        "uso": "Desarrollo web",
        "descripción": "Flask es un micro framework WSGI para aplicaciones web."
    },
    {
        "nombre_librería": "NumPy",
        "creador": "Travis Oliphant",
        "primer_año_lanzamiento": 2005,
        "versión": "1.22.0",
        "uso": "Cómputo científico",
        "descripción": "NumPy es la biblioteca fundamental para el cómputo científico en Python."
    },
    {
        "nombre_librería": "Pandas",
        "creador": "Wes McKinney",
        "primer_año_lanzamiento": 2008,
        "versión": "1.4.0",
        "uso": "Análisis de datos",
        "descripción": "pandas es una librería open source para análisis y manipulación de datos."
    },
    {
        "nombre_librería": "Matplotlib",
        "creador": "John D. Hunter",
        "primer_año_lanzamiento": 2003,
        "versión": "3.5.1",
        "uso": "Visualización de datos",
        "descripción": "Matplotlib es una librería para crear visualizaciones estáticas, animadas e interactivas en Python."
    }
    ]
    ```

🎉 ¡Felicidades! 🎉

[<< Día 18](./18_regular_expressions_sp.md) | [Día 20 >>](./20_python_package_manager_sp.md)