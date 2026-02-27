import os
os.system('cls')

# 🟢 Nivel 1 — Fundamento puro
# 1️⃣ Función simple sin retorno

# Crea una función llamada saludar() que imprima:
# Hola, bienvenido al programa
# Luego llámala 3 veces.

def bienvenida():
    '''La funcion saluda'''
    print('Hola, bienvenido al progrma')

bienvenida()

# 2️⃣ Función con parámetro

# Crea una función saludar_nombre(nombre)
# que imprima:
# Hola, Camilo
# (reemplazando por el nombre que se envíe)

def saludar(name):
    print('Hola,', name)

user_name = input('Escriba su nombre: ')
saludar(user_name)

# 3️⃣ Función que retorna valor

# Crea una función suma(a, b)
# que retorne la suma.
# Luego guarda el resultado en una variable y muéstralo.

# ⚠️ Aquí es donde empieza lo importante: return.

def suma(a, b):
    return a + b

num_a = int(input('Ingrese el primer numero que quiere sumar: '))
num_b = int(input('Ingrese el segundo numero que quiera sumar: '))

print('La suma da: ',suma(num_a, num_b))