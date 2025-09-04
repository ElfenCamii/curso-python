###
# 02 - Bucles (for)
# Permite ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

import os
os.system('cls')

print('\nBucle for: ')

# Iterar una lista
frutas = ["manzanas", "peras", "mandarinas"]
for fruta in frutas:
    print(fruta)

# Iterar sibre cualquier cosa que sea iterable
cadena = 'Camiilo'
for letra in cadena:
    print(letra)

# Enumerate()
# Enumera las propiedades que tendria una lista dada enumerate(indice y valor)
# No importa los nombres que se den 
frutas = ["manzanas", "peras", "mandarinas"]
for index, fruta in enumerate(frutas):
    print(f'El indice es {index} y la fruta es {fruta}')

# Bucles anidados
# bucles dentro de bucles
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f'{letra}{numero}')


# Break
print('\nBucle for con break')
animales = ["gato", "perro", "pez", "loro", "tortuga"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f'El loro esta escondido en el indice {idx}')
        break   # Sin el break, el bucle seguiria hasta el final de la lista aunque ya haya encontrado el loro

# Continue
print('\nBucle for con continue')
animales = ["gato", "perro", "pez", "loro", "tortuga"]
for idx, animal in enumerate(animales):
    if animal == "loro":
        continue    # Con el continue, el loro no se imprime, porque al encontrar el loro, salta esa interacción y continua con el bucle

print(animal)  # El loro no se imprime

# Comprensión de listas (List Comprehension)
animales = ["gato", "perro", "pez", "loro", "tortuga"]
animales_mayusculas = [animal.upper() for animal in animales]  # Convierte cada animal a mayusculas
print(animales_mayusculas)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)


###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
# print("\nEjercicio 1:")

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
# print("\nEjercicio 2:")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
# print("\nEjercicio 3:")

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
# print("\nEjercicio 4:")

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
# print("\nEjercicio 5:")