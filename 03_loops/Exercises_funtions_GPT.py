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

# 🟡 Nivel 2 — Aplicación lógica

# 4️⃣ Función que determina si un número es par

# Debe:

# Recibir un número
# Retornar True si es par
# Retornar False si no lo es
# Luego úsala dentro de un if.

def par(a):
    return a % 2 == 0

try:
    user_number = int(input('Escribe un numero: '))
    es_par = par(user_number)
    if es_par == True:
        print('el numero es par!')
    else:
        print('El numero es impar!')
except ValueError:
    print('No es un numero!')

# 5️⃣ Función para promedio

# Crea una función que:
# Reciba 3 números
# Retorne el promedio
# No imprimas dentro de la función.
# Imprime fuera.

# (Este detalle es clave en entrevistas.)

def promedio(a, b , c):
    return (a + b + c) / 3

try:
    user_number1 = int(input('Escribe el primer numero: '))
    user_number2 = int(input('Escribe el segundo numero: '))
    user_number3 = int(input('Escribe el tercer numero: '))

    valor_promedio = promedio(user_number1, user_number2, user_number3)

    print('El promedio de los numeros es: ', valor_promedio)
except ValueError:
    print('El valor no es un numero!')

# 🟠 Nivel 3 — Integración con lo que ya sabes

# 6️⃣ Función que cuente pares hasta N

# Debe:

# Recibir un número
# Contar cuántos pares hay desde 1 hasta ese número
# Retornar el total

# Usa for dentro de la función.

def contador(a):
    pares = 0
    for n in range(1, a + 1):
        if n % 2 == 0:
            pares += 1
    return pares
    
user_number = int(input('Ingresee un numero: '))
n_pares = contador(user_number)
print(n_pares)