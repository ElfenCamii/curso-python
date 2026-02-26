import os
os.system('cls')

# 🟢 Nivel 1 – Fundamentos

# 1️⃣ Imprimir del 1 al 10

# Usando for y range().

for n in range(1, 11):
    print(n)

# 2️⃣ Imprimir los números pares del 1 al 20

# Dos versiones:

# usando range() con salto
# usando if dentro del for
print('Solución con range()')
for n in range(2, 21, 2):
    print(n)

print('Solucion con if')
for n in range(1, 21):
    if n % 2 == 0:
        print(n)

# 3️⃣ Suma acumulada

# Pide un número al usuario e imprime la suma desde 1 hasta ese número.

# Ejemplo:
# Si ingresa 5 → resultado = 15

number_user = int(input('Ingrese un numero: '))
suma = 0
if number_user < 0:
    print('El numero tiene que ser positivo')
else:
    for n in range(1, number_user + 1):
        suma += n
    print(suma)

# 🟡 Nivel 2 – Control y lógica

# 4️⃣ Contador de positivos y negativos

# Pide 10 números al usuario y muestra:
# cuántos son positivos
# cuántos negativos
# cuántos son cero
positivos = 0
negativos = 0
cero = 0
for n in range(10):
    try:
        user_number = int(input('Escribe un numero: '))
        if user_number > 0:
            positivos += 1
        elif user_number < 0:
            negativos += 1
        else:
            cero += 1
    except ValueError:
        print('El valor ingresado no fue un numero')

print(f'El total de numeros positivos fue {positivos}')
print(f'El total de números negativos fue {negativos}')
print(f'El total de ceros fue {cero}')


# 5️⃣ Tabla de multiplicar

# Pide un número y muestra su tabla del 1 al 10 usando for.

user_number = int(input('Ingrese un numero del que quiera saber su taba de multiplicar: '))

for _ in range(1, 11):
    tabla = _ * user_number
    print(f'{_} x {user_number} = {tabla}')

# 6️⃣ Factorial

# Pide un número y calcula su factorial usando for.

# Ejemplo:
# 5 → 120

factorial = 1
try:
    user_number = int(input('Escribe el numero al que le quieres sacar el factorial: '))
    if user_number > 0 :
        for n in range(1, user_number + 1):
            factorial *= n
    else:
        print('Matematicamente hablando no se puede sacar factorial de un numero negativo')
except ValueError:
    print('El valor ingresado no es un numero')

print(f'El factorial de {user_number} es {factorial}')

# 🟠 Nivel 3 – Más razonamiento

# 7️⃣ Número mayor

# Pide 7 números y determina cuál es el mayor sin usar max().

import os
os.system('cls')

print('Numero mayor')
print('Cualquier intento no valido sera contado igualmente')

mayor = None

for n in range(7):
    try:
        user_number = int(input('Escriba un numero: '))
        if mayor is None or user_number > mayor:
            mayor = user_number
    except ValueError:
        print('El valor ingresado no es un numero entero')
    
print('El numero mayor es: ',mayor)

# 8️⃣ Promedio sin listas

# Pide 8 números y calcula el promedio.
# (No usar listas, solo acumulador y contador).

suma = 0
contador = 0

for n in range(8):
    try:
        user_number = int(input('Escribe un numero: '))
        suma += user_number
        contador += 1
    except ValueError:
        print('El valor ingresado no es valido')

if contador > 0:
    print(f'El promedio es {suma / contador}')
else:
    print('No se ingresaron numeros validos')

# 9️⃣ Contar divisores

# Pide un número y determina cuántos divisores tiene.

# Ejemplo:
# 6 → divisores: 1,2,3,6 → total 4

while True:
    divisores = []
    
    try:
        user_number = int(input('Escribe un numero: '))
        for n in range(1, (user_number + 1)):
            if user_number % n == 0:
                divisores.append(n)
        print(f'Los numeros divisores de {user_number} son')
        print(divisores)
        print('Y el total de divisores es: ', len(divisores))
        break
    except ValueError:
        print('El valor ingresado no es valido')