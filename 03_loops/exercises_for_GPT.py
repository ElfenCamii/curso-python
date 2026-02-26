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