# Reto de 30 días de Python: Día 29 - Construyendo una API

- [Día 29](#día-29)
- [Construyendo una API](#construyendo-una-api)
  - [Estructura de la API](#estructura-de-la-api)
  - [Obtener datos con GET](#obtener-datos-con-get)
  - [Obtener un documento por ID](#obtener-un-documento-por-id)
  - [Crear datos con POST](#crear-datos-con-post)
  - [Actualizar con PUT](#actualizar-con-put)
  - [Eliminar documentos con DELETE](#eliminar-documentos-con-delete)
- [💻 Ejercicio: Día 29](#-ejercicio-día-29)

## Día 29

## Construyendo una API

En esta sección presentaremos una API RESTful que utiliza métodos HTTP como GET, PUT, POST y DELETE para manejar datos.

Una API RESTful es una interfaz de programación de aplicaciones (API) que usa solicitudes HTTP para GET, PUT, POST y DELETE datos. En secciones anteriores aprendimos Python, Flask y MongoDB. Aprovecharemos ese conocimiento para desarrollar una API RESTful usando Python, Flask y MongoDB. Toda aplicación con operaciones CRUD (Crear, Leer, Actualizar, Eliminar) suele exponer una API para crear datos en la base, obtener datos, actualizarlos o borrarlos.

Los navegadores solo manejan solicitudes GET. Por eso necesitamos una herramienta que nos permita manejar todos los métodos (GET, POST, PUT, DELETE).

Ejemplos de APIs:

- API de países: https://restcountries.eu/rest/v2/all
- API de razas de gatos: https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/) es una herramienta muy popular en el desarrollo de APIs. Si quieres seguir esta sección, descarga [Postman](https://www.getpostman.com/). Una alternativa a Postman es [Insomnia](https://insomnia.rest/download).

![Postman](../images/postman.png)

### Estructura de la API

Un endpoint de API es una URL que ayuda a recuperar, crear, actualizar o eliminar un recurso. La estructura suele ser:
Ejemplo de endpoint:
https://api.twitter.com/1.1/lists/members.json
Este endpoint devuelve los miembros de una lista específica. Las listas privadas muestran miembros solo si el usuario autenticado posee la lista.
El nombre de la empresa va seguido de la versión y del propósito de la API.
Métodos:
Métodos HTTP: método y URL

La API usa los siguientes métodos HTTP para operar sobre objetos:

```sh
GET        para recuperar objetos
POST       para crear objetos y operaciones relacionadas
PUT        para actualizar objetos
DELETE     para eliminar objetos
```

Construiremos una API para recopilar información sobre estudiantes de 30DaysOfPython. Recogemos nombre, país, ciudad, año de nacimiento, habilidades y biografía.

Para implementar esta API utilizaremos:

- Postman
- Python
- Flask
- MongoDB

### Obtener datos con GET

En este paso usaremos datos ficticios y los devolveremos como JSON. Para retornarlos como JSON usaremos el módulo json y Response.

```py
# importar flask

from flask import Flask,  Response
import json

app = Flask(__name__)

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    student_list = [
        {
            'name':'Mark',
            'country':'Philippines',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')


if __name__ == '__main__':
    # usado en despliegue
    # para que funcione en producción y desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Si solicitas http://localhost:5000/api/v1.0/students en el navegador obtendrás:

![GET en navegador](../images/get_on_browser.png)

Si solicitas la misma URL en Postman obtendrás:

![GET en Postman](../images/get_on_postman.png)

En lugar de datos ficticios, conectaremos la aplicación Flask a MongoDB y obtendremos datos desde la base.

```py
# importar flask

from flask import Flask,  Response
import json
import pymongo


app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://ribzcoi:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
#Nota: nunca incluyas credenciales reales en el código.
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')


if __name__ == '__main__':
    # usado en despliegue
    # para que funcione en producción y desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Al conectar Flask con MongoDB podemos obtener la colección students de la base thirty_days_of_python:

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Mark",
        "country": "Philippines",
        "city": "Helsinki",
        "age": 38
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8c"
        },
        "name": "David",
        "country": "UK",
        "city": "London",
        "age": 34
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8e"
        },
        "name": "Sami",
        "country": "Philippines",
        "city": "Helsinki",
        "age": 25
    }
]
```

### Obtener un documento por ID

Podemos acceder a un documento individual por su ID. Por ejemplo, accedamos a Asabeneh:
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
# importar flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo


app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://ribzcoi:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
#Nota: nunca incluyas credenciales reales en el código.
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # usado en despliegue
    # para que funcione en producción y desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Respuesta de ejemplo:

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Mark",
        "country": "Philippines",
        "city": "Helsinki",
        "age": 38
    }
]
```

### Crear datos con POST

Usamos el método POST para crear datos.

```py
# importar flask

from flask import Flask,  Response, Request
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime



app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://ribzcoi:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
#Nota: nunca incluyas credenciales reales en el código.
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return ;
def update_student (id):
if __name__ == '__main__':
    # usado en despliegue
    # para que funcione en producción y desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Actualizar con PUT

```py
# importar flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime


app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://ribzcoi:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
#Nota: nunca incluyas credenciales reales en el código.
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # este decorador crea la ruta para actualizar
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, {"$set": student})
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
def update_student (id):
if __name__ == '__main__':
    # usado en despliegue
    # para que funcione en producción y desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Eliminar documentos con DELETE

```py
# importar flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime


app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://ribzcoi:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
#Nota: nunca incluyas credenciales reales en el código.
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # este decorador crea la ruta para actualizar
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, {"$set": student})
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return ;
@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.students.delete_one({"_id":ObjectId(id)})
    return
if __name__ == '__main__':
    # usado en despliegue
    # para que funcione en producción y desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## 💻 Ejercicio: Día 29

1. Implementa los ejemplos anteriores y desarrolla [esta API](https://thirtydayofpython-api.herokuapp.com/)

🎉 ¡Felicidades! 🎉

[<< Día 28](./28_API_sp.md) | [Día 30 >>](./30_conclusions_sp.md)