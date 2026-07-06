<div align="center">
  <h1>30 Días de Python: Día 11 - Funciones</h1>
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

[<< Día 10](./10_loops_sp.md) | [Día 12 >>](./12_modules_sp.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 11](#-día-11)
  - [Funciones](#funciones)
    - [Definir funciones](#definir-funciones)
    - [Declarar y llamar a una función](#declarar-y-llamar-a-una-función)
    - [Función sin parámetros](#función-sin-parámetros)
    - [Funciones que retornan valores - Parte 1](#funciones-que-retornan-valores---parte-1)
    - [Funciones con parámetros](#funciones-con-parámetros)
    - [Pasar argumentos por clave y valor](#pasar-argumentos-por-clave-y-valor)
    - [Funciones que retornan valores - Parte 2](#funciones-que-retornan-valores---parte-2)
    - [Funciones con parámetros por defecto](#funciones-con-parámetros-por-defecto)
    - [Número arbitrario de argumentos](#número-arbitrario-de-argumentos)
    - [Parámetros por defecto y arbitrarios en funciones](#parámetros-por-defecto-y-arbitrarios-en-funciones)
    - [Función como parámetro de otra función](#función-como-parámetro-de-otra-función)
  - [💻 Ejercicios: Día 11](#-ejercicios-día-11)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)
    - [Ejercicios: Nivel 3](#ejercicios-nivel-3)

# 📘 Día 11

## Funciones

Hasta ahora hemos aprendido muchas funciones integradas de Python. En esta sección nos centraremos en funciones definidas por el usuario. ¿Qué es una función? Antes de crear funciones, entendamos qué es y por qué las necesitamos.

### Definir funciones

Una función es un bloque de código reutilizable o una sentencia de programación que realiza una tarea específica. Para definir o declarar una función, Python provee la palabra clave def. La sintaxis para definir funciones es la siguiente. El código dentro de la función solo se ejecuta cuando la llamamos o la invocamos.

### Declarar y llamar a una función

Cuando creamos una función, decimos que la declaramos. Cuando la usamos, decimos que la llamamos o invocamos. Las funciones pueden tener parámetros o no.

```py
# Sintaxis
# Declarar una función
def function_name():
    codes
    codes
# Llamar a una función
function_name()
```

### Función sin parámetros

Una función puede declararse sin parámetros.

**Ejemplo:**

```py
def generate_full_name ():
    first_name = 'Mark'
    last_name = 'Ribaldz'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # Llamar a una función

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Funciones que retornan valores - Parte 1

Una función también puede devolver un valor; si una función no tiene return, devuelve None. Reescribamos las funciones anteriores usando return. A partir de ahora, cuando llamemos a la función y la imprimamos, obtendremos un valor.

```py
def generate_full_name ():
    first_name = 'Mark'
    last_name = 'Ribaldz'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### Funciones con parámetros

En una función podemos pasar diferentes tipos de datos (números, cadenas, booleanos, listas, tuplas, diccionarios o sets) como parámetros.

- Parámetro único: si una función necesita un parámetro, la llamamos con un argumento.

```py
  # Sintaxis
  # Declarar una función
  def function_name(parameter):
    codes
    codes
  # Llamar a la función
  print(function_name(argument))
```

**Ejemplo:**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Mark'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Dos parámetros: una función puede no tener parámetros o tener uno o varios. Si necesita dos parámetros, la llamamos con dos argumentos.

```py
  # Sintaxis
  # Declarar una función
  def function_name(para1, para2):
    codes
    codes
  # Llamar a la función
  print(function_name(arg1, arg2))
```

**Ejemplo:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Mark','Ribaldz'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # El valor necesita convertirse a cadena primero
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Pasar argumentos por clave y valor

Si pasamos argumentos por clave=valor, el orden de los parámetros no importa.

```py
# Sintaxis
# Declarar una función
def function_name(para1, para2):
    codes
    codes
# Llamar a la función
print(function_name(para1 = 'John', para2 = 'Doe')) # el orden de los parámetros no importa
```

**Ejemplo:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Mark', lastname = 'Ribaldz'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # el orden no importa
```

### Funciones que retornan valores - Parte 2

Si no retornamos un valor en una función, por defecto devuelve _None_. Para devolver un valor usamos la palabra clave _return_ seguida de la variable a retornar. Podemos devolver cualquier tipo de dato desde una función.

- Devolver cadenas:
  **Ejemplo:**

```py
def print_name(firstname):
    return firstname
print_name('Mark') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Mark', lastname='Ribaldz')
```

- Devolver números:

**Ejemplo:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
```

- Devolver booleanos:
  **Ejemplo:**

```py
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # la instrucción return detiene la ejecución adicional en la función
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Devolver listas:
  **Ejemplo:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Funciones con parámetros por defecto

A veces pasamos valores por defecto a los parámetros. Si no proporcionamos un argumento al llamar la función, se usa el valor por defecto.

```py
# Sintaxis
# Declarar una función
def function_name(param = value):
    codes
    codes
# Llamar a la función
function_name()
function_name(arg)
```

**Ejemplo:**

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Mark'))

def generate_full_name (first_name = 'Mark', last_name = 'Ribaldz'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # gravedad promedio en la superficie de la Tierra
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - gravedad promedio en la Tierra
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravedad en la Luna
```

### Número arbitrario de argumentos

Si no sabemos cuántos argumentos se pasarán a la función, podemos usar un parámetro con * para aceptar un número arbitrario de argumentos.

```py
# Sintaxis
# Declarar una función
def function_name(*args):
    codes
    codes
# Llamar a la función
function_name(param1, param2, param3,..)
```

**Ejemplo:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # equivalente a total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Parámetros por defecto y arbitrarios en funciones

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Mark','Brook','David','Eyob'))
```

### Función como parámetro de otra función

```py
# Puedes pasar una función como argumento
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 Has avanzado mucho. ¡Sigue así! Has completado el desafío del día 11 y ya llevas 11 pasos en el camino al éxito. Ahora realiza algunos ejercicios para ejercitar la mente y la práctica.

## Testimonios

Es hora de expresar tu opinión sobre el autor y 30DaysOfPython. Puedes dejar tu testimonio en este [enlace](https://testimonify.herokuapp.com/).

## 💻 Ejercicios: Día 11

### Ejercicios: Nivel 1

1. Declara una función _add_two_numbers_. Debe aceptar dos parámetros y devolver su suma.
2. La fórmula del área de un círculo es: area = π x r x r. Escribe una función _area_of_circle_ que la calcule.
3. Escribe una función llamada add_all_nums que acepte un número arbitrario de argumentos y sume todos. Verifica que todos los elementos sean de tipo numérico. Si no, devuelve un mensaje apropiado.
4. La temperatura en Celsius (°C) se puede convertir a Fahrenheit (°F) con: °F = (°C x 9/5) + 32. Escribe una función _convert_celsius_to_fahrenheit_.
5. Escribe una función llamada check_season que acepte un mes y devuelva la estación: otoño, invierno, primavera o verano.
6. Escribe una función llamada calculate_slope que devuelva la pendiente de una ecuación lineal.
7. La ecuación cuadrática se calcula como: ax² + bx + c = 0. Escribe una función _solve_quadratic_eqn_ que calcule las soluciones.
8. Declara una función llamada print_list que acepte una lista y imprima cada elemento.
9. Declara una función llamada reverse_list que acepte un arreglo y devuelva su reverso (usa un bucle).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
```

10. Declara una función capitalize_list_items que acepte una lista y devuelva una lista con los elementos en mayúscula.
11. Declara una función add_item que acepte una lista y un ítem. Debe devolver la lista con el ítem agregado al final.

```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
```

12. Declara una función remove_item que acepte una lista y un ítem. Debe devolver la lista con el ítem eliminado.

```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Declara una función sum_of_numbers que acepte un número y sume todos los números en ese rango.

```py
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
```

14. Declara una función sum_of_odds que acepte un número y sume todos los impares en ese rango.
15. Declara una función sum_of_even que acepte un número y sume todos los pares en ese rango.

### Ejercicios: Nivel 2

1. Declara una función evens_and_odds que acepte un entero positivo y calcule la cantidad de pares e impares en ese número.

```py
    print(evens_and_odds(100))
    # La cantidad de números pares es 50.
    # La cantidad de números impares es 50.
```

2. Llama a tu función factorial que acepte un entero y devuelva su factorial.
3. Llama a tu función _is_empty_ que acepte un argumento y verifique si está vacío.
4. Escribe distintas funciones que acepten listas y calculen: media, mediana, moda, rango, varianza y desviación estándar.

### Ejercicios: Nivel 3

1. Escribe una función is_prime que verifique si un número es primo.
2. Escribe una función que verifique si todos los ítems en una lista son únicos.
3. Escribe una función que verifique si todos los ítems en una lista son del mismo tipo de dato.
4. Escribe una función que verifique si una variable proporcionada es un nombre de variable válido en Python.
5. Accede al archivo de datos countries-data.py.

- Crea una función llamada the_most_spoken_languages que devuelva las 10 o 20 lenguas más habladas en el mundo, ordenadas de mayor a menor.
- Crea una función llamada the_most_populated_countries que devuelva los 10 o 20 países más poblados del mundo, ordenados de mayor a menor.

🎉 ¡Felicidades! 🎉

[<< Día 10](./10_loops_sp.md) | [Día 12 >>](./12_modules_sp.md)
