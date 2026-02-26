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