<div align="center">
  <h1> 30 días de Python: Día 5 - Listas</h1>
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

[<< Día 4](./04_strings_sp.md) | [Día 6 >>](./06_tuples_sp.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Día 5](#día-5)
  - [Listas](#listas)
    - [Cómo crear listas](#cómo-crear-listas)
    - [Acceder por índice positivo](#acceder-por-índice-positivo)
    - [Acceder por índice negativo](#acceder-por-índice-negativo)
    - [Desempaquetado de listas](#desempaquetado-de-listas)
    - [Slicing de listas](#slicing-de-listas)
    - [Modificar listas](#modificar-listas)
    - [Buscar elementos](#buscar-elementos)
    - [Agregar elementos](#agregar-elementos)
    - [Insertar elementos](#insertar-elementos)
    - [Eliminar elementos](#eliminar-elementos)
    - [Eliminar con pop()](#eliminar-con-pop)
    - [Eliminar con del](#eliminar-con-del)
    - [Vaciar la lista](#vaciar-la-lista)
    - [Copiar listas](#copiar-listas)
    - [Unir listas](#unir-listas)
    - [Contar elementos](#contar-elementos)
    - [Encontrar el índice de un elemento](#encontrar-el-índice-de-un-elemento)
    - [Invertir listas](#invertir-listas)
    - [Ordenar listas](#ordenar-listas)
  - [💻 Ejercicios - Día 5](#-ejercicios---día-5)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)

# Día 5

## Listas

En Python hay cuatro tipos de colecciones:

- List: colección ordenada y mutable. Permite elementos duplicados.
- Tuple: colección ordenada e inmutable. Permite elementos duplicados.
- Set: colección no ordenada e indexable; no permite duplicados (aunque se pueden añadir elementos).
- Dictionary: colección no ordenada, mutable y accesible por clave. No permite claves duplicadas.


Una lista es una colección ordenada y mutable que puede contener elementos de diferentes tipos. Una lista puede estar vacía o contener elementos heterogéneos.

### Cómo crear listas

En Python podemos crear listas de dos maneras:

- Usando la función incorporada `list()`

```py
# Sintaxis
lst = list()
```

```py
empty_list = list() # Esta es una lista vacía
print(len(empty_list)) # 0
```
- Usando corchetes `[]`

```py
# Sintaxis
lst = []
```

```py
empty_list = [] # Esta es una lista vacía
print(len(empty_list)) # 0
```

Listas con valores iniciales. Usamos `len()` para comprobar la longitud.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # lista de frutas
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # lista de verduras
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # lista de animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # lista de web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Imprimir listas y su longitud
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```

```sh
Salida
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```

- Las listas pueden contener elementos de distintos tipos

```py
 lst = ['Mark', 250, True, {'country':'Philippines', 'city':'Helsinki'}] # lista con distintos tipos de datos
```


### Acceder por índice positivo

Usamos índices para acceder a los elementos de una lista. Los índices comienzan en 0. La imagen muestra claramente dónde empiezan los índices.

![List index](../images/list_index.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # estamos usando su índice para acceder al primer elemento
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

### Acceder por índice negativo

Los índices negativos cuentan desde el final; `-1` es el último elemento, `-2` el penúltimo.

![List negative indexing](../images/list_negative_indexing.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

### Desempaquetado de listas

```py
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

```

```py
# Ejemplo uno
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Ejemplo dos
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Ejemplo tres
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```

### Slicing de listas

- Índices positivos: especificando inicio, fin y paso obtenemos una nueva lista. (inicio por defecto 0, fin por defecto len(lst) - 1, paso por defecto 1)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # devuelve todos los elementos
# mismo resultado que arriba
all_fruits = fruits[0:] # Si no se especifica el índice de fin, devolverá todos los elementos desde el inicio hasta el final
orange_and_mango = fruits[1:3] # no incluye el índice 3
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # usamos el tercer parámetro (paso). Toma cada 2 elementos - ['banana', 'mango']
```

- Índices negativos: especificando inicio, fin y paso con índices negativos se obtiene una nueva lista.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # Devuelve todos los elementos
orange_and_mango = fruits[-3:-1] # No incluye el último elemento, ['orange', 'mango']
orange_mango_lemon = fruits[-3:] # Devuelve los elementos desde -3 hasta el final, ['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # un paso negativo invierte la lista, ['lemon', 'mango', 'orange', 'banana']
```

### Modificar listas

Una lista es una colección ordenada y mutable. A continuación modificamos la lista `fruits`.


```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

### Buscar elementos

Use el operador `in` para comprobar si un elemento es miembro de una lista. Véase el ejemplo.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### Agregar elementos

Para añadir un elemento al final de una lista usamos el método `append()`.

```py
# Sintaxis
lst = list()
lst.append(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

### Insertar elementos

Podemos usar el método *insert()* para insertar un elemento en un índice específico de la lista. Ten en cuenta que los demás elementos se desplazarán a la derecha. El método *insert()* recibe dos parámetros: el índice y el elemento a insertar.


```py
# Sintaxis
lst = ['item1', 'item2']
lst.insert(index, item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # inserta 'apple' entre 'orange' y 'mango'
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

### Eliminar elementos

- Usa el método *remove()* para eliminar un elemento específico de la lista

```py
# Sintaxis
lst = ['item1', 'item2']
lst.remove(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - este método elimina la primera aparición del elemento en la lista
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

### Eliminar con `pop()`

Usa `pop()` para eliminar el elemento en el índice dado (si no se indica, elimina el último elemento):

```py
# Sintaxis
lst = ['item1', 'item2']
lst.pop()       # Último elemento
lst.pop(index)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

### Eliminar con `del`

Usa la palabra clave *del* para eliminar un índice específico, también puede eliminar un rango de índices o eliminar por completo la lista


```py
# Sintaxis
lst = ['item1', 'item2']
del lst[index] # Elimina solo un elemento
del lst        # Elimina la lista completa
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # elimina elementos en el rango dado; no eliminará el elemento con índice 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # Esto producirá: NameError: name 'fruits' is not defined
```

### Vaciar listas

Usa `clear()` para vaciar una lista:

```py
# Sintaxis
lst = ['item1', 'item2']
lst.clear()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

### Copiar listas

Puedes copiar una lista reasignándola a una nueva variable: `list2 = list1`. En ese caso `list2` referencia el mismo objeto; los cambios se reflejarán en ambos. Si quieres una copia independiente usa el método `copy()`.

```py
# Sintaxis
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon'] (copia de la lista)
```

### Unir listas

Hay varias formas de concatenar o unir dos o más listas.

- Suma (+)

```py
# Sintaxis
list3 = list1 + list2
```

```py
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

- Usar el método *extend()*
El método *extend()* puede anexar una lista a otra. Véase el ejemplo a continuación.

```py
# Sintaxis
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
```

```py
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### Contar elementos

Usa el método *count()* para devolver el número de veces que aparece un elemento en la lista:


```py
# Sintaxis
lst = ['item1', 'item2']
lst.count(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### Encontrar el índice de un elemento

El método *index()* devuelve el índice de un elemento en la lista:

```py
# Sintaxis
lst = ['item1', 'item2']
lst.index(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, primera aparición
```

### Invertir listas

Usa el método *reverse()* para invertir el orden de la lista.

```py
# Sintaxis
lst = ['item1', 'item2']
lst.reverse()

```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

### Ordenar listas

Para ordenar una lista podemos usar el método *sort()* o la función incorporada *sorted()*. El método *sort()* reordena la lista en orden ascendente y modifica la lista original. Si el parámetro reverse de *sort()* es True, ordenará la lista en orden descendente.

- sort(): Este método modifica la lista original

  ```py
  # Sintaxis
  lst = ['item1', 'item2']
  lst.sort()                # ascending
  lst.sort(reverse=True)    # descending
  ```

  **Ejemplo:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits.sort()
  print(fruits)             # ordenadas alfabéticamente, ['banana', 'lemon', 'mango', 'orange']
  fruits.sort(reverse=True)
  print(fruits) # ['orange', 'mango', 'lemon', 'banana']
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  ages.sort()
  print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
 
  ages.sort(reverse=True)
  print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
  ```

  sorted(): No modifica la lista original; devuelve una nueva lista

  **Ejemplo:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
  # Reverse order
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits,reverse=True)
  print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
  ```



🌕 Muy bien, has avanzado mucho. Acabas de completar el desafío del día 5. Ahora realiza algunos ejercicios para practicar.

## 💻 Ejercicios - Día 5

### Ejercicios: Nivel 1

1. Declara una lista vacía
2. Declara una lista con más de 5 elementos
3. Encuentra la longitud de la lista
4. Obtén el primer, medio y último elemento de la lista
5. Declara una lista llamada `mixed_data_types` que contenga tu nombre, edad, altura, estado civil y dirección
6. Declara una lista `it_companies` e inicialízala con: Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
7. Imprime la lista usando `print()`
8. Imprime el número de empresas en la lista
9. Imprime la primera, la del medio y la última empresa
10. Cambia el nombre de una de las empresas y vuelve a imprimir la lista
11. Agrega una empresa IT a `it_companies`
12. Inserta una empresa IT en la mitad de la lista
13. Cambia el nombre de una empresa en `it_companies` a mayúsculas (¡excepto IBM!)
14. Une `it_companies` en una cadena usando la cadena '#;&nbsp; '
15. Verifica si una empresa existe en `it_companies`
16. Ordena la lista usando el método `sort()`
17. Invierte la lista en orden descendente usando `reverse()`
18. Corta (slice) las primeras 3 empresas de la lista
19. Corta (slice) las últimas 3 empresas de la lista
20. Corta la(s) empresa(s) del medio de la lista
21. Elimina la primera empresa IT de la lista
22. Elimina la(s) empresa(s) del medio de la lista
23. Elimina la última empresa IT de la lista
24. Elimina todas las empresas IT de la lista
25. Destruye la lista `it_companies`
26. Concatena las siguientes listas:

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```
27. Inserta 'Python' y 'SQL' después de `full_stack` en la lista concatenada.

### Ejercicios: Nivel 2

1. A continuación, una lista con las edades de 10 estudiantes:

```py
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- Ordena la lista y encuentra la edad máxima y mínima
- Agrega la edad mínima y máxima nuevamente a la lista
- Encuentra la mediana de las edades (un elemento medio o el promedio de dos elementos medios)
- Encuentra la edad promedio (suma de todos los elementos dividida por su cantidad)
- Encuentra el rango de edades (máximo - mínimo)
- Compara |min - promedio| y |max - promedio| usando la función `abs()`

1. Encuentra el país del medio en la [lista de países](https://github.com/Taki-Ta/30-Days-Of-Python-Simplified_Chinese_Version/tree/master/data/countries.py)
2. Divide la lista de países en dos listas iguales (si es par; si no, la primera lista tendrá un país más)
3. Para la lista ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'], separa los tres primeros países de los países nórdicos restantes.

🎉 ¡Felicidades! 🎉

[<< Día 4](./04_strings_sp.md) | [Día 6 >>](./06_tuples_sp.md)
