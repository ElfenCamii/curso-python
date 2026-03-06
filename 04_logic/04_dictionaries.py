###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

import os
os.system('cls')

# Ejemplo de diccionario tipico
persona = {
  "nombre": "Camiilo",
  "edad": 331,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@ElfenCamii",
    "instagram": "@ElfenCamii",
    "facebook": "ElfenCamii"
  }
}

# Para acceder a los valores
print(persona['nombre'])
print(persona['calificaciones'][2])
print(persona['socials']['twitter'])

# Cambiar valores al acceder
persona['nombre'] = 'Camii'
persona['calificaciones'][2] = 10

# Para eliminar completamente una propieda
del persona['edad']
print(persona)

# Para eliminar pero conservar la información 
es_estudiante = persona.pop('es_estudiante')
print(f'es_estudiante: {es_estudiante}')
print(persona)

# Sobre escribir un diccionario con otro diccionario
a = {'name': 'Camii', 'age': 31}
b = {'name': 'Danny', 'es_estudiante': True}
a.update(b)

print(a)

# Para saber si existe una propiedad
print('name' in persona)
print('nombre' in persona)

# Obtener todas las claves
print('\nkeys:')
print(persona.keys())

# Obtener todos los valores
print('\nvalues:')
print(persona.values())

# Obtener tanto clave como valor
print('\nitems:')
print(persona.items())

# Para obtener por un lado la llave y por otro el valor
for key, value in persona.items():
    print(f'\n{key}: {value}')

# Para saber si hay un valor dentro del diccionario sin que salte error
print(persona.get('casa', 'El valor buscado no existe!'))

# Para saber la longitud de un diccionario
print(len(persona))

# para limpiar un diccionaro (eliminar los valores)
persona.clear()

# Para eliminar el ultimo elemento del diccionario
persona.popitem()

# Para copiar un diccionario
persona_2 = persona.copy()

# Otra forma de copiar un diccionario
persona_3 = dict(persona)

# Para recorrer diccionarios anidados

mi_familia = {
    'mama' : {
      'nombre' : 'Ana',
      'edad' : 52
    },
    'hermana' : {
        'nombre' : 'Maria',
        'edad' : 22
    },
    'pareja' : {
        'nombre' : 'Daniella',
        'edad' : '23'
    }   
}

for x, obj in mi_familia.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y]) 

# Para crear un diccionaro en base a otros diccionarios

mama = {
      'nombre' : 'Ana',
      'edad' : 52
    }

hermana = {
        'nombre' : 'Maria',
        'edad' : 22
    }

pareja = {
        'nombre' : 'Daniella',
        'edad' : '23'
    }

mi_familia_2 = {
    'mama' : mama,
    'hermana' : hermana,
    'novia' : pareja
}

print(mi_familia_2)