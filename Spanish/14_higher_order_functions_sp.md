<div align="center">
  <h1>30 Días de Python: Día 14 - Funciones de orden superior</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/mark-anthony-ribaldo/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/ribzcoi">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/ribzcoi?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/mark-anthony-ribaldo/" target="_blank">Mark Anthony Ribaldo</a><br>
<small>Segunda edición: julio de 2021</small>
</sub>

</div>

[<< Día 13](./13_list_comprehension_sp.md) | [Día 15 >>](./15_python_type_errors_cn_sp.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 14](#-día-14)
  - [Funciones de orden superior](#funciones-de-orden-superior)
    - [Funciones como parámetros](#funciones-como-parámetros)
    - [Funciones como valor de retorno](#funciones-como-valor-de-retorno)
  - [Closures en Python](#closures-en-python)
  - [Decoradores en Python](#decoradores-en-python)
    - [Crear decoradores](#crear-decoradores)
    - [Aplicar varios decoradores a una función](#aplicar-varios-decoradores-a-una-función)
    - [Aceptar parámetros en decoradores](#aceptar-parámetros-en-decoradores)
  - [Funciones integradas de orden superior](#funciones-integradas-de-orden-superior)
    - [Python - función map](#python---función-map)
    - [Python - función filter](#python---función-filter)
    - [Python - función reduce](#python---función-reduce)
  - [💻 Ejercicios: Día 14](#-ejercicios-día-14)
    - [Ejercicios: Básico](#ejercicios-básico)
    - [Ejercicios: Intermedio](#ejercicios-intermedio)
    - [Ejercicios: Avanzado](#ejercicios-avanzado)

# 📘 Día 14

## Funciones de orden superior

En Python, las funciones son tratadas como ciudadanos de primera clase; se pueden hacer las siguientes operaciones con funciones:

- Una función puede recibir una o más funciones como parámetros
- Una función puede ser el valor de retorno de otra función
- Una función puede ser modificada
- Una función puede asignarse a una variable

En esta sección discutiremos:

1. Pasar funciones como parámetros
2. Devolver funciones como valores de retorno
3. Usar closures y decoradores en Python

### Funciones como parámetros

```py
def sum_numbers(nums):  # función normal
    return sum(nums)    # usa la función incorporada sum

def higher_order_function(f, lst):  # pasar función como argumento
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Funciones como valor de retorno

```py
def square(x):          # función que devuelve el cuadrado
    return x ** 2

def cube(x):            # función que devuelve el cubo
    return x ** 3

def absolute(x):        # función que devuelve el valor absoluto
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # función de orden superior que devuelve una función
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

En los ejemplos anteriores se observa que la función de orden superior devuelve distintas funciones según el parámetro pasado.

## Closures en Python

Python permite que una función anidada acceda al ámbito de su función envolvente externa. Esto se conoce como closure. Un closure en Python se crea al anidar una función dentro de otra función envolvente y devolver la función interna. Veamos un ejemplo.

**Ejemplo:**

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## Decoradores en Python

Un decorador es un patrón de diseño que permite añadir nueva funcionalidad a un objeto sin modificar su estructura. Los decoradores normalmente se usan aplicándolos antes de la definición de la función que se desea decorar.

### Crear decoradores

Para crear un decorador necesitamos una función externa que contenga una función envoltura interna.

**Ejemplo:**

```py
# función normal
def greeting():
    return 'Welcome to Python'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

# Implementando lo anterior con sintaxis de decorador

'''Esta función decoradora es una función de orden superior que acepta una función como argumento'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
```

### Aplicar varios decoradores a una función

```py
'''Estas funciones decoradoras son funciones de orden superior que reciben funciones como argumento'''

# primer decorador
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# segundo decorador
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator     # en este caso el orden importa, ya que .upper() no funciona sobre una lista
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### Aceptar parámetros en decoradores

A menudo necesitamos que nuestras funciones acepten parámetros; por eso definimos decoradores que también los aceptan.

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Mark", "Ribaldz",'Finland')
```

## Funciones integradas de orden superior

En esta sección veremos algunas funciones integradas de orden superior como map(), filter() y reduce().
Las funciones lambda se pueden pasar como argumentos; su caso de uso ideal es con map, filter y reduce.

### Python - función map

map() es una función integrada que recibe una función y un iterable como parámetros.

```py
    # sintaxis
    map(function, iterable)
```

**Ejemplo 1**

```py
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Usemos lambda
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**Ejemplo 2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**Ejemplo 3**

```py
names = ['Mark', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Usemos lambda
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

map itera sobre el iterable y devuelve un nuevo iterable transformado.

### Python - función filter

filter() llama a la función especificada que retorna un valor booleano para cada elemento del iterable y filtra los elementos que cumplen la condición.

```py
    # sintaxis
    filter(function, iterable)
```

**Ejemplo 1**

```py
# filtremos solo los pares
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**Ejemplo 2**

```py
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# filtrar nombres largos
names = ['Mark', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Mark']
```

### Python - función reduce

reduce() se define en el módulo functools; es necesario importarla desde allí. Al igual que map y filter, recibe una función y un iterable. Sin embargo, no devuelve otro iterable sino un único valor acumulado.

**Ejemplo 1**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 Ejercicios: Día 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Mark', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Ejercicios: Básico

1. Explica la diferencia entre map, filter y reduce.
2. Explica la diferencia entre funciones de orden superior, closures y decoradores.
3. Define la función que llama (ver ejemplo).
4. Imprime cada país de la lista countries usando un bucle for.
5. Imprime cada nombre de la lista names usando un bucle for.
6. Imprime cada número de la lista numbers usando un bucle for.

### Ejercicios: Intermedio

1. Usa map para convertir cada país en countries a mayúsculas y genera una nueva lista.
2. Usa map para elevar al cuadrado cada número en numbers y genera una nueva lista.
3. Usa map para convertir cada nombre en names a mayúsculas y genera una nueva lista.
4. Usa filter para filtrar países que contienen 'land'.
5. Usa filter para filtrar países con exactamente seis caracteres.
6. Usa filter para filtrar países con seis o más caracteres.
7. Usa filter para filtrar países que comienzan con 'E'.
8. Encadena dos o más iteradores de lista (por ejemplo arr.map(callback).filter(callback).reduce(callback)).
9. Declara una función get_string_lists que reciba una lista y devuelva una lista con solo los elementos de tipo cadena.
10. Usa reduce para sumar todos los números en la lista numbers.
11. Usa reduce para concatenar todos los países en una oración: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries.
12. Declara una función categorize_countries que retorne una lista de países que siguen un patrón común (puedes ver la lista de países en el archivo countries.js del repositorio, por ejemplo 'land', 'ia', 'island', 'stan').
13. Crea una función que devuelva un diccionario donde las claves sean la primera letra de los nombres de país y el valor sea el número de países que comienzan con esa letra.
14. Declara una función get_first_ten_countries que devuelva los primeros diez países de la lista countries.js en la carpeta data.
15. Declara una función get_last_ten_countries que devuelva los últimos diez países de la lista.

### Ejercicios: Avanzado

1. Usando el archivo countries_data.py (https://github.com/RibaldzZ/30-Days-Of-Python-Philippines/blob/master/data/countries-data.py), completa lo siguiente:
   - Ordena los países por nombre, capital y población.
   - Ordena y obtiene los diez idiomas más usados.
   - Ordena y obtiene los diez países con mayor población.

🎉 ¡Felicidades! 🎉

[<< Día 13](./13_list_comprehension_sp.md) | [Día 15 >>](./15_python_type_errors_cn_sp.md)
