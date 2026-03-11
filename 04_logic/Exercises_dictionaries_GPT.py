import os
os.system('cls')

# 🟢 🧱 NIVEL BASE (estructura y acceso)

# 1️⃣ Crear y acceder

# Crea un diccionario llamado persona que tenga:

# nombre
# edad
# ciudad

# Luego:

# Imprime solo el nombre.
# Imprime solo la edad.
# Imprime todo el diccionario.

persona = {
    'nombre' : 'Camiilo',
    'edad' : 31,
    'ciudad' : 'Bogotá'
}

print('El nombre es: ',persona['nombre'])
print('La edad es: ', persona['edad'])
print('Toda la info es: \n', persona)

# 2️⃣ Modificar valores

# Partiendo de un diccionario:

# producto = {
#     "nombre": "Laptop",
#     "precio": 2500,
#     "stock": 5
# }

# Haz lo siguiente:

# Cambia el precio.
# Aumenta el stock en 3.
# Imprime el diccionario actualizado.

producto = {
    "nombre": "Laptop",
    "precio": 2500,
    "stock": 5
}

producto['precio'] = 3000
producto['stock'] += 3
print('Actualizacion de productos: \n', producto)

# 3️⃣ Agregar y eliminar claves

# Crea un diccionario vacío llamado estudiante.

# Agrega nombre, carrera y semestre.
# Elimina la clave semestre.
# Verifica si la clave "edad" existe antes de intentar imprimirla.

# (Pista: usar in)

estudiante = {}

estudiante['nombre'] = 'Camii'
estudiante['carrera'] = 'Mecatrónica'
estudiante['semestre'] = 'Segunda semana'

estudiante.pop('semestre')

if 'edad' not in estudiante:
    print('La clave "Edad" no existe')
else:
    print('LA clave "edad" si existe')

print(estudiante)

# 🟡 🧠 NIVEL MEDIO (recorrer y lógica)

# 4️⃣ Recorrer claves y valores

# Dado:

# notas = {
#     "matematicas": 4.5,
#     "fisica": 3.8,
#     "quimica": 4.2
# }

# Recorre el diccionario.
# Imprime cada materia con su nota.
# Calcula el promedio usando un loop.

notas = {
    "matematicas": 4.5,
    "fisica": 3.8,
    "quimica": 4.2
}

promedio = 0
materias = 0
promedio1 = []

for materia, nota in notas.items():
    print(f'La materia es {materia} y la nota fue de {nota}')
    promedio1.append(nota)

print('El promedio de las notas es: \n', round(sum(promedio1)/len(promedio1), 2))
    
for n in notas.values():
    promedio += n
    materias += 1

print('El promedio de las notas es: \n', round((promedio)/materias, 2))


# 5️⃣ Contar ocurrencias

# Pide palabras al usuario hasta que escriba "salir".
# Guárdalas en un diccionario donde:
# La clave sea la palabra.
# El valor sea cuántas veces se repitió.
# Ejemplo resultado:

# {"hola": 3, "python": 2}

dic_palabras = {}
list_palabras = []
valor = 0

while True:
    palabras = input('\nEscribe una palabra, para terminar el programa escribe "salir": \n').lower()
    
    if palabras == 'salir':
        break
    list_palabras.append(palabras)

for palabra in list_palabras:
    if palabra in dic_palabras:
        dic_palabras[palabra] +=1
    else:
        dic_palabras[palabra] = 1

print(dic_palabras)


# 6️⃣ Filtrar por condición

# Dado un diccionario de productos con precios:

# Crea un nuevo diccionario solo con los productos que cuesten más de 1000.

productos = {
    "Laptop": 2500,
    "Mouse": 80,
    "Teclado": 150,
    "Monitor": 1200,
    "Celular": 1800,
    "Audifonos": 200,
    "Tablet": 950,
    "Impresora": 1100
}

productos_mas_100 = {}

for producto, precio in productos.items():
    if precio > 1000:
        productos_mas_100[producto] = precio
print(productos_mas_100)

# 🔴 🧩 NIVEL DIFÍCIL (estructura mental)

# 7️⃣ Diccionario de listas

# Crea un diccionario donde:

# Cada clave sea un nombre de estudiante.
# Cada valor sea una lista de 3 notas.

# Luego:

# Calcula el promedio de cada estudiante.
# Determina cuál tiene el promedio más alto.

print('!Bienvenido!')
print('Portal de profesores')

dic_estudiantes = {}
dic_promedios = {}

def promedio(lista_notas):
    return sum(lista_notas) / len(lista_notas)

while True:
    contador = 0
    notas = []
    print('Desea agregar un estudiante?')
    continuar = input('Escriba si/salir: ').lower()
    if continuar == 'salir':
        print('Gracias, nos vemos en la proxima!')
        break
    estudiante = input('Escribe el nombre del estudiante: \n')
    while contador < 3:
        nota = float(input('Agregue las notas del estudiante: '))
        notas.append(nota)
        contador += 1
    dic_estudiantes[estudiante] = notas
    dic_promedios[estudiante] = promedio(notas)


print('Los promedios de los estudiantes son: ', dic_promedios)

mayor  = max(dic_promedios.values())
for nombre, max_promedio in dic_promedios.items():
    if max_promedio == mayor:
        print(f'El estudiante con mayor promedio es {nombre} y es de {max_promedio}')

    
# 8️⃣ Diccionario anidado

# Crea un sistema tipo agenda:

# agenda = {
#     "Camilo": {"telefono": "123", "ciudad": "Bogotá"},
#     "Ana": {"telefono": "456", "ciudad": "Medellín"}
# }

# Permite buscar una persona y mostrar sus datos.
# Maneja el caso donde no exista.

agenda = {
    "Camilo": {"telefono": "123", "ciudad": "Bogotá"},
    "Ana": {"telefono": "456", "ciudad": "Yopal"},
    "Daniella": {"telefono": "890", "ciudad": "Medellín"}
}

print('----------------------------------------')
print('--- Bienvenidos a tu agenda personal ---')
print('----------------------------------------')

while True:
    print('''
\nEscribe el número de la opción que desees:
          
    1. Buscar a una persona
    2. Salir
''')
    
    try:
        user = int(input('Que deseas hacer: '))
        if user == 2:
            print('--------------------------')
            print('-------- Gracias! --------')
            print('--- Hasta la proxima!! ---')
            print('--------------------------')
            break
        elif user == 1:
            user_persona = input('\nIngrese el nombre de la persona que desea buscar: ').strip().capitalize()
            print(f'\nIngresaste el nombre de → {user_persona}')
            if agenda.get(user_persona):
                for number, city in agenda[user_persona].items():
                    print(f'{number} : {city}')
            else:
                print(agenda.get(user_persona, 'La persona buscada no se encuentra en la agenda'))
    except ValueError:
        print('\nEl valor ingresado no es un número')
        print('Intente nuevamente, gracias!')

# 9️⃣ Conteo de pares usando diccionario

# Dada una lista de números:
# Crea un diccionario con:

# "pares": cantidad
# "impares": cantidad

# Usando tu función par().

def par(a):
    return a % 2 == 0

list_number = [39, 58, 56, 68, 28, 49, 66, 52, 12, 7, 45, 45, 48, 23, 52, 31, 45, 46, 63, 15]
list_par = []
list_impar = []
dict_number = {}
dict_par = {}
dict_impar = {}

for number in list_number:
    if par(number):
        list_par.append(number)
        
    else:
        list_impar.append(number)

total_par = len(list_par)
total_impar = len(list_impar)

dict_par['lista_pares'] = list_par
dict_par['total_pares'] = total_par
dict_impar['lista_impares'] = list_impar
dict_impar['total_impares'] = total_impar

dict_number['pares'] = dict_par
dict_number['impares'] = dict_impar
print(dict_number)

# 🟣 🔥 RETO (para mañana)

# Sistema de inventario simple:

# Usar un diccionario donde:

# clave → nombre del producto
# valor → cantidad disponible

# El programa debe:

# Permitir agregar producto.
# Permitir actualizar cantidad.
# Mostrar inventario.
# Eliminar producto.

# Salir.

# Todo usando funciones.