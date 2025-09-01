###
# 04 - variables
# las variables sirven para guardar datos en memoria
#python es un lenguaje de tipado dinamico, y de tipado fuerte
# no es necesario declarar el tipo de dato de una variable
# una variable puede cambiar de tipo de dato en cualquier momento
###

# asignacion de variables
# solo hace falta poner el nombre de la variable, el signo = y el valor a asignar
my_name = "camilo"

print(my_name)

age = 31
print(age)

age = 32
print(age)  # la variable age se puede cambiar de valor en cualquier momento

# Tipado dinamico: el tipado de dato de una variable puede cambiar en cualquier momento
# ya que se determina en tiempo de ejecucion yno tiene que ser declarado

name = "juan"
print(type (name))

name = 123
print(type (name))  # la variable name cambio de tipo de dato de str a int

# tipado fuerte: no se pueden mezclar tipos de datos diferentes en operaciones
# print("mi nombre es " + 123) # error, no se puede concatenar str con int

print(f"hola {my_name}, tengo {age + 5} años")  # f-string permite mezclar tipos de datos diferentes en una misma cadena

# convenciones para nombrar variables
mi_nombre_de_variable = "ok"  # snake_case
nombre = "ok" 

MiNombreDeVariable = "no"  # PascalCase (no recomendado para variables)
minombredevariable = "no"  # lowercase (no recomendado para variables)

mi_nombre_de_variable_123 = "ok"  # se pueden usar numeros pero no al inicio

MI_CONSTANTE = "ok"  # mayusculas con guion bajo para constantes (no recomendado para variables)

#nombres no validos de variables
# 1nombre = "no" # no puede empezar con numero
# mi-nombre = "no" # no puede tener guion medio
# mi nombre = "no" # no puede tener espacios
# def = "no" # no puede ser una palabra reservada de python

# palabras reservadas de python
# and       del       from      None      True   as        elif      global    nonlocal  try 
# False     else      if        not       while  assert    except    import    or        with
# break     finally   in        pass      yield  class     for       is        raise
# continue  lambda    return
# def       await     async
# (estas palabras no se pueden usar como nombres de variables)

