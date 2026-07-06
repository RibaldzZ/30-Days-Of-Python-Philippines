<div align="center">
  <h1> 30 Dias de Python: Dia 2 - Variables, Funciones integradas</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/mark-anthony-ribaldo/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/ribzcoi">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/ribzcoi?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/mark-anthony-ribaldo/" target="_blank">Mark Anthony Ribaldo</a><br>
<small> First Edition: July, 2026</small>
</sub>

</div>

[<< Dia 1](../readme.md) | [Dia 3 >>](../03_Day_Operators/03_operators.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 2](#-día-2)
   - [Funciones integradas](#funciones-integradas)
   - [Variables](#variables)
     - [Declaración de múltiples variables en una línea](#declaración-de-múltiples-variables-en-una-línea)
   - [Tipos de datos](#tipos-de-datos)
   - [Comprobación de tipos de datos y conversión](#comprobación-de-tipos-de-datos-y-conversión)
   - [Números](#números)
   - [💻 Ejercicios - Día 2](#💻-ejercicios---día-2)
     - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
     - [Ejercicios: Nivel 2](#ejercicios-nivel-2)

# 📘 Dia 2

## Funciones integradas

En Python tenemos muchas funciones integradas. Las funciones integradas están disponibles globalmente para su uso, lo que significa que puede hacer uso de las funciones integradas sin importarlas ni configurarlas. Algunas de las funciones integradas de Python más utilizadas son las siguientes: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_ y _dir()_ . En la siguiente tabla, verá una lista exhaustiva de las funciones integradas de Python sacadas de la [documentación de Python](https://docs.python.org/3.9/library/functions.html).

![Funciones integradas](../../images/builtin-functions.png)

Abramos el shell de Python y comencemos a usar algunas de las funciones integradas más comunes.

![Funciones integradas](../../images/builtin-functions_practice.png)

Practiquemos más usando diferentes funciones integradas

![Funciones integradas de ayuda y directorio](../../images/help_and_dir_builtin.png)

Como puede ver en la terminal de arriba, Python tiene palabras reservadas. No usamos palabras reservadas para declarar variables o funciones. En la siguiente sección cubriremos las variables.

Creo que a estas alturas ya está familiarizado con las funciones integradas. Hagamos una práctica más de funciones integradas y pasaremos a la siguiente sección.

![Suma mín. máx.](../../images/builtin-functional-final.png)

## Variables

Las variables almacenan datos en la memoria de una computadora. Se recomienda el uso de variables mnemotécnicas en muchos lenguajes de programación. Una variable mnemotécnica es un nombre de variable que se puede recordar y asociar fácilmente. Una variable se refiere a una dirección de memoria en la que se almacenan los datos.
Número al principio, carácter especial o guión no están permitidos al nombrar una variable. Una variable puede tener un nombre corto (como x, y, z), pero se recomienda enfáticamente un nombre más descriptivo (nombre, apellido, edad, país).

Reglas de nombres de variables de Python

- Un nombre de variable debe comenzar con una letra o el carácter de subrayado
- Un nombre de variable no puede comenzar con un número
- Un nombre de variable solo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y \_)
- Los nombres de las variables distinguen entre mayúsculas y minúsculas (firstname, Firstname, FirstName y FIRSTNAME) son variables diferentes)

Estos son algunos ejemplos de nombres de variables válidos:

```shell
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # si queremos usar palabra reservada como variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

Nombres de variables no válidos

```shell
first-name
first@name
first$name
num-1
1num
```

Usaremos el estilo estándar de nomenclatura de variables de Python que ha sido adoptado por muchos desarrolladores de Python. Los desarrolladores de Python usan la convención de nomenclatura de variables de caja de serpiente (snake_case). Usamos un carácter de subrayado después de cada palabra para una variable que contiene más de una palabra (p. ej., nombre, apellido, velocidad de rotación del motor). El siguiente ejemplo es un ejemplo de nomenclatura estándar de variables, se requiere guión bajo cuando el nombre de la variable es más de una palabra.

Cuando asignamos un determinado tipo de datos a una variable, se llama declaración de variable. Por ejemplo, en el siguiente ejemplo, mi nombre se asigna a una variable first_name. El signo igual es un operador de asignación. Asignar significa almacenar datos en la variable. El signo igual en Python no es la igualdad como en Matemáticas.

_Ejemplo:_

```py
# Variables en Python
first_name = 'Mark'
last_name = 'Ribaldz'
country = 'Philippines'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Mark',
   'lastname':'Ribaldz',
   'country':'Philippines',
   'city':'Helsinki'
   }
```

Usemos las funciones integradas _print()_ y _len()_. La función de impresión toma un número ilimitado de argumentos. Un argumento es un valor que se puede pasar o poner dentro del paréntesis de la función, vea el ejemplo a continuación.

**Ejemplo:**

```py
print('Hello, World!') # El texto Hola, Mundo! es un argumento
print('Hello',',', 'World','!') # Puede tomar varios argumentos, se han pasado cuatro argumentos
print(len('Hello, World!')) # solo se necesita un argumento
```

Imprimamos y también encontremos la longitud de las variables declaradas en la parte superior:

**Ejemplo:**

```py
# Imprimiendo los valores almacenados en las variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### Declaración de múltiples variables en una línea

También se pueden declarar múltiples variables en una línea:

**Ejemplo:**

```py
first_name, last_name, country, age, is_married = 'Mark', 'Ribaldz', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

Obtener la entrada del usuario usando la función integrada _input()_. Asignemos los datos que obtenemos de un usuario a las variables first_name y age.
**Ejemplo:**

```py
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```

## Tipos de datos

Hay varios tipos de datos en Python. Para identificar el tipo de datos usamos la función incorporada _type_. Me gustaría pedirle que se concentre en comprender muy bien los diferentes tipos de datos. Cuando se trata de programar, todo se trata de tipos de datos. Introduje los tipos de datos desde el principio y viene de nuevo, porque todos los temas están relacionados con los tipos de datos. Cubriremos los tipos de datos con más detalle en sus respectivas secciones.

## Comprobación de tipos de datos y conversión

- Verificar tipos de datos: para verificar el tipo de datos de ciertos datos/variables usamos el _type_
   **Ejemplo:**

```py
# Diferentes tipos de datos en python
# Declaremos variables con varios tipos de datos

first_name = 'Mark'     # str
last_name = 'Ribaldz'       # str
country = 'Philippines'         # str
city= 'Helsinki'            # str
age = 250                   # int, no es mi edad real, no te preocupes

# Imprimir tipos
print(type('Mark'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Mark','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
```

- Casting: Conversión de un tipo de dato a otro tipo de dato. Usamos _int()_, _float()_, _str()_, _list_, _set_
   Cuando hacemos operaciones aritméticas, los números de cadena deben convertirse primero a int o float; de lo contrario, devolverá un error. Si concatenamos un número con una cadena, el número debe convertirse primero en una cadena. Hablaremos sobre la concatenación en la sección String.

   **Ejemplo:**

```py
# int a float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float a int
gravity = 9.81
print(int(gravity))             # 9

# int a str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str a int o float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str a list
first_name = 'Mark'
print(first_name)               # 'Mark'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

## Números

Tipos de datos numéricos en Python:

1. Integers: números enteros (negativos, cero y positivos)
    Ejemplo:
    ... -3, -2, -1, 0, 1, 2, 3...

2. Floating: números de coma (números decimales)
    Ejemplo:
    ... -3,5, -2,25, -1,0, 0,0, 1,1, 2,2, 3,5...

3. Complex: números complejos
    Ejemplo:
    1 + j, 2 + 4j, 1 - 1j

🌕 Eres increíble. Acaba de completar los desafíos del día 2 y está dos pasos por delante en su camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios - Día 2

### Ejercicios: Nivel 1

1. Dentro de 30DaysOfPython crea una carpeta llamada day_2. Dentro de esta carpeta crea un archivo llamado variables.py
2. Escriba un comentario de python que diga 'Día 2: 30 días de programación en python'
3. Declarar una variable de nombre y asignarle un valor
4. Declarar una variable de apellido y asignarle un valor
5. Declare una variable de nombre completo y asígnele un valor
6. Declarar una variable de país y asignarle un valor
7. Declarar una variable de ciudad y asignarle un valor
8. Declarar una variable de edad y asignarle un valor
9. Declarar una variable de año y asignarle un valor
10. Declarar una variable is_married y asignarle un valor
11. Declarar una variable is_true y asignarle un valor
12. Declare una variable is_light_on y asígnele un valor
13. Declarar múltiples variables en una línea

### Ejercicios: Nivel 2

1. Verifique el tipo de datos de todas sus variables usando la función incorporada type()
1. Usando la función incorporada _len()_, encuentre la longitud de su nombre
1. Compara la longitud de tu nombre y tu apellido
1. Declarar 5 como num_one y 4 como num_two
     1. Sume num_one y num_two y asigne el valor a un total variable
     2. Reste num_two de num_one y asigne el valor a una variable diff
     3. Multiplique num_two y num_one y asigne el valor a un producto variable
     4. Divide num_one por num_two y asigna el valor a una división variable
     5. Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a un residuo variable
     6. Calcula num_one a la potencia de num_two y asigna el valor a una variable exp
     7. Encuentra la división de piso de num_one por num_two y asigna el valor a una variable floor_division
1. El radio de un círculo es de 30 metros.
     1. Calcule el área de un círculo y asigne el valor a una variable con el nombre de _area_of_circle_
     2. Calcule la circunferencia de un círculo y asigne el valor a una variable con el nombre de _circum_of_circle_
     3. Tome el radio como entrada del usuario y calcule el área.
1. Use la función de entrada integrada para obtener el nombre, el apellido, el país y la edad de un usuario y almacene el valor en sus nombres de variables correspondientes
1. Ejecute la ayuda ('palabras clave') en el shell de Python o en su archivo para verificar las palabras o palabras clave reservadas de Python

🎉 ¡FELICITACIONES! 🎉

[<< Day 1](../readme.md) | [Day 3 >>](../03_Day_Operators/03_operators.md)
