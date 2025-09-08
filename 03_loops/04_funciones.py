###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

''' Definición de una función 

def nombre_de_la_funcion(parametro1, parametro2, ....):
    # docstring
    # cuerpo de la función
    return valor_de_retorno # opcional

'''

# Ejemplo de una función para imprimr algo en consola
def saludar():
    print('Hola')
saludar()

# #Ejemplo de una función con parametro
def saludar_a(nombre):
    print(f'Hola!! {nombre}')

saludar_a('Camiilo')
saludar_a('Daniella')
saludar_a('Ana')
saludar_a('Sebas')
saludar_a('Kevin')

# El parámetro es lo que acepta la función
# El argumento es el que le pasamos nosotros

# Funciones con más parámetros
def suma(a, b):
    suma = a + b
    return suma

result = suma(2, 3)
print(result)

# Documentar las funciones con docstring
def restar(a, b):
    '''Resta dos números y devuelve el resultado'''
    return a - b

print(restar.__doc__)       # Se usa .__doc__ para acceder a la documentación de una función 

# Parámetros por defecto
def multiplicar(a, b = 2):
    return a * b
print(multiplicar(2))
print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre, edad, sexo):
    print(f'Soy {nombre}, tengo {edad} años y me identifico como {sexo}')

# Parámetros son posicionales
describir_persona('Camiilo', 31, 'Dios')
describir_persona('hombre', 'Sebas', 31)

# Argumentos por clave
# Parámetros nombrados

describir_persona(sexo='pez', nombre='Camii', edad=31)

# Argumentos de longitud de variables (*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs)
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')

mostrar_informacion_de(nombre='Camii', edad=31, sexo='pez')
print('\n')
mostrar_informacion_de(name='Danny' ,edad=22, country='Colombia')
print('\n')
mostrar_informacion_de(nick='Campos' ,es_pendejo=True, is_rich=True)
print('\n')
mostrar_informacion_de(super_name='Kevin' ,es_calvo=True, gatos=True)

