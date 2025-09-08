# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().

print("\nEjercicio 1: Números con range")

for num in range(0, 10):
    num += 1
    if num < 10:
        print(f'El número es {num} o,')
    elif num == 10:
        print(f'Llegamos al número {num}')

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().

print("\nEjercicio 2: Numeros impares")

for num in range(0, 20):
    num += 1
    if num == 1 or num % 2 != 0:
        print(f'El {num} es un número impar')

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().

print("\nEjercicio 3: Múltipos de 5")

mul_5 = []

for num in range (1, 51):
    if num % 5 == 0:
        mul_5.append(num)
print(mul_5)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().

print("\nEjercicio 4: Números inversos")

inv_num = []
for num in range (10, 0, -1):
    inv_num.append(num)
print(inv_num)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().

print("\nEjercicio 5: Suma de números")

sum_num = []
for num in range(0, 101):
    sum_num.append(num)
sum_total = sum(sum_num)
print(sum_num)
print(sum_total)

# Coprobación:

suma = sum(range(1, 101))
print(suma)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().

import time

print("\nEjercicio 6: Tablas de multiplicar")
user = int(input('Introduce un número: '))
for num in range(1, 11):
    print(f'{user} x {num} = {user * num}')
    time.sleep(0.25)