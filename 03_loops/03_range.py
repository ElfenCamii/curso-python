###
# 03 - range()
# Permite crear una secuencia de numeros. Puede ser útil para for, pero no solo para eso
###

print('\nrange():')

nums = range(5)     # (5) Va del 0 al 5 porque si no se pone nada como primer valor se asume que es 0
print(nums)         # No crea una lista con los numeros del 0 al 5 sino un rango de 0 a 5 para cuando 
                      # Para cuando se necesite

# Genera una secuencia de números del 0 al 9
for num in range(10):
    print(num)

# range(inicio, fin)
for num in range(5, 10):
    print(num)

# range(inicio, fin, paso)
for num in range(0, 100, 5):
    print(num)

for num in range(-5, 0):
    print(num)

# range(10, 0, -1) Cuenta en negativo
for num in range(10, 0, -1):
    print(num)

# range no es una lista crea los numeros sobre la marcha
nums = range(10)
list_of_noms = list(nums)
print(list_of_noms)

# uno de range para hacer algo un numero repetido de veces 
# for _ in range(5):
#     print('Hace cinco veces algo')

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
# print("\nEjercicio 1:")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
# print("\nEjercicio 2:")

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
# print("\nEjercicio 3:")

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
# print("\nEjercicio 4:")

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
# print("\nEjercicio 5:")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
# print("\nEjercicio 6:")