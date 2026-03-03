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