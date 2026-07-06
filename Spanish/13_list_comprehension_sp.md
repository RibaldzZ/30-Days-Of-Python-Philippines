<div align="center">
  <h1>30 Días de Python: Día 13 - Comprensiones de listas</h1>
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

[<< Día 12](./12_modules_sp.md) | [Día 14 >>](./14_higher_order_functions_sp.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 13](#📘-día-13)
  - [Comprensiones de listas](#comprensiones-de-listas)
  - [Funciones lambda](#funciones-lambda)
    - [Crear una función lambda](#crear-una-función-lambda)
    - [Funciones lambda dentro de otra función](#lambda-dentro-de-otra-función)
  - [💻 Ejercicios: Día 13](#💻-ejercicios-día-13)

# 📘 Día 13

## Comprensiones de listas

En Python, las comprensiones de listas son una forma concisa de crear listas a partir de secuencias. Es una manera corta de crear nuevas listas a partir de secuencias. Las comprensiones de listas son más rápidas que iterar sobre listas con un bucle for.

```py
# sintaxis
[i for i in iterable if expresión]
```

**Ejemplo 1**

Por ejemplo, si quieres convertir una cadena en una lista de caracteres, puedes hacerlo de varias formas. Veamos algunas:

```py
# un método
language = 'Python'
lst = list(language)  # convertir la cadena en lista
print(type(lst))      # list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']

# segunda forma: comprensión de listas
lst = [i for i in language]
print(type(lst))      # list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']
```

**Ejemplo 2**

Por ejemplo, si quieres generar una lista de números:

```py
# generar números
numbers = [i for i in range(11)]  # genera números de 0 a 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# también puedes hacer operaciones matemáticas durante la iteración
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# también se pueden generar listas de tuplas
numbers = [(i, i * i) for i in range(11)]
print(numbers)                    # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

**Ejemplo 3**

Las comprensiones de listas pueden combinarse con expresiones if:

```py
# generar números pares
even_numbers = [i for i in range(21) if i % 2 == 0]  # genera pares de 0 a 20
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# generar números impares
odd_numbers = [i for i in range(21) if i % 2 != 0]  # genera impares de 0 a 20
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# filtrar números: obtengamos los pares positivos
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)           # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# aplanar una lista 2D
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)                  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Funciones lambda

Las funciones lambda son pequeñas funciones anónimas sin nombre. Pueden aceptar cualquier número de argumentos, pero solo una expresión. Las funciones lambda son similares a las funciones anónimas en JavaScript. Son útiles cuando necesitamos una función anónima dentro de otra función.

### Crear una función lambda

Para crear una función lambda usamos la palabra clave lambda, seguido de uno o más parámetros y luego una expresión. La función lambda no usa return explícito; devuelve la expresión implícitamente.

```py
# sintaxis
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

**Ejemplo:**

```py
# función nombrada
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))  # 5

# con lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))  # 5

# lambda autoejecutable
print((lambda a, b: a + b)(2, 3))  # 5

square = lambda x: x ** 2
print(square(3))    # 9
cube = lambda x: x ** 3
print(cube(3))      # 27

# múltiples variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # 22
```

### Funciones lambda dentro de otra función

Uso de lambda dentro de otra función:

```py
def power(x):
    return lambda n: x ** n

cube = power(2)(3)   # la función power ahora se usa con dos pares de paréntesis
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32
```

🌕 Sigue con el buen trabajo. Mantente motivado; el cielo es tu límite. Has completado el desafío del Día 13 y has dado 13 pasos hacia algo grandioso. Ahora ejercita tu mente y sigue practicando.

## 💻 Ejercicios: Día 13

1. Usa una comprensión de listas para filtrar los números negativos y ceros de la siguiente lista:
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. Aplana la siguiente lista de listas a una lista unidimensional:

   ```py
   list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

   Salida:
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. Crea la siguiente lista de tuplas usando una comprensión de listas:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
4. Aplana la siguiente estructura en una nueva lista:
   ```py
   countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
   Salida:
   [['Finlandia', 'FIN', 'Helsinki'], ['Suecia', 'SWE', 'Estocolmo'], ['Noruega', 'NOR', 'Oslo']]
   ```
5. Convierte la siguiente lista en una lista de diccionarios:
   ```py
   countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
   Salida:
   [{'País': 'Finlandia', 'Ciudad': 'Helsinki'},
    {'País': 'Suecia', 'Ciudad': 'Estocolmo'},
    {'País': 'Noruega', 'Ciudad': 'Oslo'}]
   ```
6. Convierte la siguiente lista en una lista de cadenas concatenadas:
   ```py
   names = [[('Mark', 'Ribaldz')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   Salida:
   ['Mark Anthony Ribaldo', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
7. Escribe una función lambda que calcule la pendiente o la ordenada al origen de una función lineal.

🎉 ¡Felicidades! 🎉

[<< Día 12](./12_modules_sp.md) | [Día 14 >>](./14_higher_order_functions_sp.md)
