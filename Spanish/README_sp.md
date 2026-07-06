# 🐍 30 Días de Python

| # Día |                                           Tema                                           |
| ------ | :--------------------------------------------------------------------------------------: |
|   01   |                                   [Introducción](./readme_sp.md)                                    |
|   02   | [Variables y funciones integradas](./02_variables_builtin_functions_sp.md) |
|   03   |                       [Operadores](./03_operators_sp.md)                       |
|   04   |                         [Cadenas](./04_strings_sp.md)                         |
|   05   |                            [Listas](./05_lists_sp.md)                            |
|   06   |                           [Tuplas](./06_tuples_sp.md)                           |
|   07   |                             [Conjuntos](./07_sets_sp.md)                             |
|   08   |                     [Diccionarios](./08_dictionaries_sp.md)                     |
|   09   |                     [Condicionales](./09_conditionals_sp.md)                     |
|   10   |                            [Bucles](./10_loops_sp.md)                            |
|   11   |                        [Funciones](./11_functions_sp.md)                        |
|   12   |                          [Módulos](./12_modules_sp.md)                          |
|   13   |             [Comprensión de listas](./13_list_comprehension_sp.md)             |
|   14   |         [Funciones de orden superior](./14_higher_order_functions_sp.md)         |
|   15   |             [Errores de tipo](./15_python_type_errors_sp.md)             |
|   16   |            [Fechas y horas en Python](./16_python_datetime_sp.md)            |
|   17   |             [Manejo de excepciones](./17_exception_handling_sp.md)             |
|   18   |           [Expresiones regulares](./18_regular_expressions_sp.md)           |
|   19   |                  [Manejo de archivos](./19_file_handling_sp.md)                  |
|   20   |         [Gestor de paquetes](./20_python_package_manager_sp.md)         |
|   21   |            [Clases y objetos](./21_classes_and_objects_sp.md)            |
|   22   |                   [Web scraping](./22_web_scraping_sp.md)                   |
|   23   |            [Entornos virtuales](./23_virtual_environment_sp.md)            |
|   24   |                       [Estadística](./24_statistics_sp.md)                       |
|   25   |                          [Pandas](./25_pandas_sp.md)                          |
|   26   |                   [Python en la web](./26_python_web_sp.md)                    |
|   27   |       [Python y MongoDB](./27_python_with_mongodb_sp.md)        |
|   28   |                              [API](./28_API_sp.md)                               |
|   29   |                   [Construir API](./29_building_API_sp.md)                   |
|   30   |                      [Conclusiones](./30_conclusions_sp.md)                      |

🧡🧡🧡 Feliz codificación 🧡🧡🧡

<div>
<small>Ayuda al <strong>autor</strong> a crear más material educativo</small> <br />  
<a href=""><img src='.././images/paypal_lg.png' alt='Paypal Logo' style="width:10%"/></a>
</div>

<div align="center">
  <h1> 30 Días de Python: Día 1 - Introducción</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/mark-anthony-ribaldo/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/ribzcoi">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/ribzcoi?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/mark-anthony-ribaldo/" target="_blank">Mark Anthony Ribaldo</a><br>
<small> Segunda edición: julio de 2021</small>
</sub>

</div>

[Ir al Día 2 >>](./02_variables_builtin_functions_sp.md)

![30DaysOfPython](.././images/30DaysOfPython_banner3@2x.png)

- [🐍 30 Días de Python](#-30-días-de-python)
- [📘 Día 1](#-día-1)
  - [¡Bienvenido!](#¡bienvenido!)
  - [Introducción](#introducción)
  - [¿Por qué elegir Python?](#¿por-qué-elegir-python?)
  - [Configuración del entorno](#configuración-del-entorno)
    - [Instalar Python](#instalar-python)
    - [Python Shell](#python-shell)
    - [Instalar Visual Studio Code](#instalar-visual-studio-code)
      - [Cómo usar Visual Studio Code](#cómo-usar-visual-studio-code)
  - [Fundamentos de Python](#fundamentos-de-python)
    - [Sintaxis de Python](#sintaxis-de-python)
    - [Indentación en Python](#indentación-en-python)
    - [Comentarios](#comentarios)
- [Ejemplo: comentario de una sola línea](#ejemplo-comentario-de-una-sola-línea)
- [Ejemplo: comentario multilínea (docstring)](#ejemplo-comentario-multilínea-docstring)
    - [Tipos de datos](#tipos-de-datos)
      - [Números](#números)
      - [Cadenas](#cadenas)
      - [Booleanos](#booleanos)
      - [Listas](#listas)
      - [Diccionarios](#diccionarios)
      - [Tuplas](#tuplas)
      - [Conjuntos](#conjuntos)
    - [Comprobar tipos de datos](#comprobar-tipos-de-datos)
    - [Archivos Python](#archivos-python)
  - [💻 Ejercicios - Día 1](#-ejercicios---día-1)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)
    - [Ejercicios: Nivel 3](#ejercicios-nivel-3)

# 📘 Día 1

## ¡Bienvenido!

**Felicidades** por decidir participar en el desafío de programación _30 Días de Python_. En este reto aprenderás todo lo necesario para convertirte en programador Python y la mayoría de los conceptos de programación. Al finalizar el reto recibirás un certificado del desafío _30DaysOfPython_.

Si quieres participar activamente, únete al grupo de Telegram [30DaysOfPython challenge](https://t.me/+YourLinkHere).

## Introducción

Python es un lenguaje de programación de alto nivel, de propósito general. Es un lenguaje de código abierto, interpretado y orientado a objetos. Python fue creado por el programador holandés Guido van Rossum. El nombre del lenguaje proviene del show cómico británico _Monty Python's Flying Circus_. La primera versión se lanzó el 20 de febrero de 1991. Este desafío de 30 días te ayudará a aprender progresivamente la versión más reciente de Python, Python 3. Cada día cubre un tema diferente con explicaciones claras, ejemplos del mundo real, y muchos ejercicios y proyectos prácticos.

El reto es adecuado para principiantes y profesionales que quieran aprender Python. Completar el reto puede tomar de 30 a 100 días; los miembros activos del grupo de Telegram tienen más probabilidades de terminarlo.

Este reto fue escrito inicialmente en inglés sencillo, y luego traducido al chino. El reto es motivador, accesible y desafiante. Requiere dedicación para completarlo. Si aprendes mejor con vídeos, visita el canal RibaldzZ Channel en YouTube: <a href="https://www.youtube.com/@ribaldzz">
RibaldzZ Channel YouTube channel</a>. Puedes empezar por el video [Python for absolute beginners](https://youtu.be/OCCWZheOesI). Suscríbete, deja tus preguntas en los comentarios y sé proactivo; el autor te podrá notar.

El autor aprecia tus comentarios, que compartas el contenido y la retroalimentación sobre el reto 30DaysOfPython. Puedes dejar feedback aquí: [link]()

## ¿Por qué elegir Python?

Python es un lenguaje con sintaxis cercana al lenguaje humano, sencillo y fácil de aprender y usar.
Python es usado en muchas industrias y empresas (incluido Google). Se usa para desarrollar aplicaciones web, de escritorio, administración de sistemas y librerías de aprendizaje automático. Python está ampliamente adoptado en la comunidad de ciencia de datos y machine learning. Si esto no te convence, ¡es hora de empezar!

## Configuración del entorno

### Instalar Python

Para ejecutar scripts escritos en Python necesitas instalar Python. Visita la página de descargas de Python: [https://www.python.org/](https://www.python.org/).

Si usas Windows haz clic en el botón marcado en la imagen.

[![Instalar en Windows](.././images/installing_on_windows.png)](https://www.python.org/)

Si usas macOS haz clic en el botón marcado en la imagen.

[![Instalar en macOS](.././images/installing_on_macOS.png)](https://www.python.org/)

Para comprobar si Python está instalado, abre la terminal y ejecuta:

```shell
python --version
```

![Versión de Python](../images/python_versio.png)

En mi terminal aparece Python 3.7.5. Tu versión puede variar, pero debe ser 3.6 o superior. Si ves la versión, Python está instalado. Continúa al siguiente apartado.

### Python Shell

Python es un lenguaje interpretado, no necesita compilación. Se ejecuta línea por línea. Python incluye el Python Shell (intérprete interactivo), también llamado REPL (Read Eval Print Loop). Se usa para ejecutar comandos Python individuales y ver resultados al instante.

El Python Shell espera código Python. Al escribir código lo interpreta y muestra el resultado.
Abre la terminal o el símbolo del sistema (cmd) y escribe:

```shell
python
```

![Python Scripting Shell](../images/opening_python_shell.png)

El intérprete interactivo de Python estará abierto y mostrará el prompt >>> para que escribas comandos Python. Escribe tu primer script y pulsa Enter.
Veamos un ejemplo en el Shell interactivo.

![Script Python en el shell](../images/adding_on_python_shell.png)

Genial: escribiste tu primer script en el Shell interactivo. ¿Cómo salir del Shell?
Para salir escribe **exit()** y pulsa Enter.

![Salir del shell de Python](../images/exit_from_shell.png)

Ahora sabes cómo abrir y cerrar el intérprete interactivo.

Si escribes código inválido, Python mostrará un error. Probemos un error intencional:

![Error de sintaxis inválida](../images/invalid_syntax_error.png)

El error indica Syntax Error: Invalid Syntax. Usar x para multiplicar no es válido en Python; el operador correcto es el asterisco (*). El error señala exactamente lo que hay que corregir.

El proceso de encontrar y corregir errores se llama depuración (debugging). Reemplazamos x por * y volvemos a ejecutar:

![Corrigiendo Error de sintaxis](../images/fixing_syntax_error.png)

El error se corrige y el código produce el resultado esperado. Verás errores así a diario; aprender a depurar es esencial. Para depurar bien debes reconocer los tipos de errores: SyntaxError, IndexError, NameError, ModuleNotFoundError, KeyError, ImportError, AttributeError, TypeError, ValueError, ZeroDivisionError, etc. Los explicaremos más adelante.

Practiquemos más en el Python Shell. Abre la terminal y escribe python.

![Python Scripting Shell](../images/opening_python_shell.png)

Con el Shell abierto hagamos operaciones matemáticas básicas: suma, resta, multiplicación, división, módulo y potencia.

Antes de programar, hagamos algunos cálculos:

- 2 + 3 = 5
- 3 - 2 = 1
- 3 * 2 = 6
- 3 / 2 = 1.5
- 3 ** 2 = 9

En Python también tenemos:

- 3 % 2 = 1 => resto de la división
- 3 // 2 = 1 => división entera (sin resto)

Conviértelo a código Python en el Shell. Primero escribe un comentario.

Un comentario es texto ignorado por Python. Sirve para documentar y mejorar la legibilidad. En Python los comentarios empiezan con #.
Así se escribe un comentario en Python:

```python
# Los comentarios comienzan con una almohadilla
# Este es un comentario en Python porque empieza con (#)
```

![Operaciones en el shell de Python](../images/maths_on_python_shell.png)

Antes de continuar, practica más: cierra el Shell con _exit()_ y vuelve a abrirlo; escribe texto en el Shell:

![Escribir cadena en el shell de Python](./images/writing_string_on_shell.png)

### Instalar Visual Studio Code

El Python Shell está bien para probar fragmentos, pero para proyectos más grandes se usan editores de código. En este reto usaremos Visual Studio Code. VS Code es un editor de texto de código abierto muy popular. Recomiendo instalar Visual Studio Code, aunque puedes usar otro editor si lo prefieres.

[![Visual Studio Code](../images/vscode.png)](https://code.visualstudio.com/)

Si ya tienes Visual Studio Code, veamos cómo usarlo.
Si prefieres vídeos, mira el tutorial de instalación y configuración de VS Code para Python: https://www.youtube.com/watch?v=bn7Cx4z-vSo

#### Cómo usar Visual Studio Code

Abre Visual Studio Code haciendo doble clic en su icono. Aparecerá la interfaz. Interactúa con los iconos marcados en la imagen.

![Visual Studio Code](../images/vscode_ui.png)

Crea en el escritorio una carpeta llamada 30DaysOfPython. Ábrela con Visual Studio Code.

![Abrir proyecto en Visual Studio](../images/how_to_open_project_on_vscode.png)

![Abrir un proyecto](../images/opening_project.png)

Dentro del proyecto verás accesos para crear archivos y carpetas. Yo creé el primer archivo helloworld.py; tú puedes hacer lo mismo.

![Crear archivo Python](../images/helloworld.png)

Cuando termines de programar puedes cerrar el proyecto desde el editor:

![Cerrar proyecto abierto](../images/closing_opened_project.png)

¡Enhorabuena! El entorno está listo. ¡Manos a la obra!

## Fundamentos de Python

### Sintaxis de Python

Los scripts Python se pueden escribir en el Shell interactivo o en un editor. Los archivos Python usan la extensión .py.

### Indentación en Python

La indentación son espacios en blanco en el código. En muchos lenguajes se usa para mejorar legibilidad; en Python se usa para definir bloques de código. En otros lenguajes se usan llaves. Un error común en Python es el error de indentación.

![Error de indentación](../images/indentation.png)

### Comentarios

Los comentarios son importantes para la legibilidad. Python no ejecuta el texto dentro de comentarios.
Cualquier texto que comience con # en Python es un comentario.

# Ejemplo: comentario de una sola línea

```shell
# Este es el primer comentario
# Este es el segundo comentario
# Python se está apoderando del mundo
```

# Ejemplo: comentario multilínea (docstring)

Se pueden usar comillas triples para comentarios multilínea si no se asignan a una variable.

```shell
"""Este es un comentario multilínea
Los comentarios multilínea ocupan varias líneas.
Python se está apoderando del mundo
"""
```

### Tipos de datos

Python tiene varios tipos de datos. Empecemos por los más comunes. Veremos otros tipos más en detalle en secciones posteriores. A continuación un resumen para familiarizarte.

#### Números

- Enteros: ... -3, -2, -1, 0, 1, 2, 3 ...
- Flotantes: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- Complejos: 1 + j, 2 + 4j

#### Cadenas

Texto entre comillas simples o dobles; para multilínea se usan comillas triples.

**Ejemplos:**

```py
'Mark'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
```

#### Booleanos

True o False. Deben estar en mayúscula.

**Ejemplo:**

```python
True  # ¿La luz está encendida? Si sí, el valor es True
False # ¿La luz está encendida? Si no, el valor es False
```

#### Listas

Lista ordenada que puede contener distintos tipos, similar a un array en JavaScript.

**Ejemplos:**

```py
[0, 1, 2, 3, 4, 5] # todos números
['Banana', 'Orange', 'Mango', 'Avocado'] # todos cadenas
['Finland','Estonia', 'Sweden','Norway'] # todos cadenas (países)
['Banana', 10, False, 9.81] # mezcla de tipos
```

#### Diccionarios

Colección no ordenada de pares clave:valor.

**Ejemplo:**

```py
{
'first_name':'Mark',
'last_name':'Ribaldz',
'country':'Philippines',
'age':250,
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
```

#### Tuplas

Colección ordenada e inmutable.

**Ejemplo:**

```py
('Mark', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # nombres
```

```py
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planetas
```

#### Conjuntos

Colección no ordenada que almacena elementos únicos (sin duplicados).

**Ejemplos:**

```py
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # el orden en un set no importa
```

Detallaremos cada tipo de dato en secciones posteriores.

### Comprobar tipos de datos

Usa la función built-in **type** para comprobar el tipo de una variable. En la imagen puedes ver ejemplos:

![Comprobando tipos de datos](../images/checking_data_types.png)

### Archivos Python

Abre tu carpeta de proyecto 30DaysOfPython (créala si no existe). Dentro crea helloworld.py. Repite lo que hicimos en el Shell pero usando print() para ver resultados en consola desde un archivo.

En el intérprete se imprime sin print, pero en VS Code debes usar la función _print()_. Ejemplo de uso: _print('argumento1', 'argumento2')_.

**Ejemplo:** archivo helloworld.py

```py
# Día 1 - Desafío 30DaysOfPython

print(2 + 3)             # Suma (+)
print(3 - 1)             # Resta (-)
print(2 * 3)             # Multiplicación (*)
print(3 / 2)             # División (/)
print(3 ** 2)            # Potencia (**)
print(3 % 2)             # Módulo (%)
print(3 // 2)            # División entera (//)

# Comprobar tipos de datos
print(type(10))          # entero
print(type(3.14))        # flotante
print(type(1 + 3j))      # complejo
print(type('Mark'))  # cadena
print(type([1, 2, 3]))   # lista
print(type({'name':'Mark'})) # diccionario
print(type({9.8, 3.14, 2.7}))    # conjunto
print(type((9.8, 3.14, 2.7)))    # tupla
```

Para ejecutar el archivo: en VS Code usa el botón verde o en la terminal escribe _python helloworld.py_.

![Ejecutando script Python](../images/running_python_script.png)

Genial. Completaste el Día 1. Practica con los ejercicios siguientes.

## 💻 Ejercicios - Día 1

### Ejercicios: Nivel 1

1. Comprueba la versión de Python que usas.
2. Abre el Python Shell e intenta con los operandos 3 y 4:
   - Suma (+)
   - Resta (-)
   - Multiplicación (*)
   - Módulo (%)
   - División (/)
   - Potencia (**)
   - División entera (//)
3. En el Python Shell escribe las siguientes cadenas:
   - Tu nombre
   - Tu apellido
   - Tu país
   - Estoy disfrutando 30 días de Python
4. Comprueba el tipo de los siguientes datos:
   - 10
   - 9.8
   - 3.14
   - 4 - 4j
   - ['Mark', 'Python', 'Finland']
   - Tu nombre
   - Tu apellido
   - Tu país

### Ejercicios: Nivel 2

1. Crea en la carpeta 30DaysOfPython una carpeta llamada day_1. Dentro crea helloworld.py y repite las preguntas 1, 2, 3 y 4. Recuerda usar _print()_ en archivos. Navega a la carpeta donde guardaste el archivo y ejecútalo.

### Ejercicios: Nivel 3

1. Escribe ejemplos para distintos tipos de datos en Python: números (enteros, flotantes, complejos), cadenas, booleanos, listas, tuplas, conjuntos y diccionarios.
2. Calcula la distancia euclídea entre (2, 3) y (10, 8): [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance).

🎉 ¡Felicidades! 🎉

[Ir al Día 2 >>](./02_variables_builtin_functions_sp.md)
