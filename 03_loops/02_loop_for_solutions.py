###
# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
###

import os
os.system('cls')

print("\nEjercicio 1: Números pares")

for pares in range(1, 21):
    if pares % 2 == 0:
        print(pares)


###
# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
###

print("\nEjercicio 2: Mediana de una lista")

numeros = [10, 20, 30, 40, 50]
num = []
suma = sum(numeros)
print(suma)
for numero in numeros:
    num.append(numero)
    total = sum(num)
print(total)


###
# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
###

print("\nEjercicio 3: Maximo de una lista")

numeros = [15, 5, 25, 10, 20]
mayor = []
print(max(numeros))

for numero in numeros:
    mayor.append(numero)
print(max(mayor))


###
# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
###

print("\nEjercicio 4: Filtado por longitud")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]

mas_de5 = [palabra for palabra in palabras if len(palabra) > 5]
print(mas_de5)


###
# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
###

print("\nEjercicio 5: Contar palabras que empiecen con: ")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
user = input('Introduce una letra: ')
user_letter = user.lower()
palabras_letra = []

for letra in palabras:
    if user_letter == letra[0]:
        palabras_letra.append(letra)

if palabras_letra != []:
    print(f'Las palabras de la lista que tienen la letra {user} son: \n{palabras_letra}')
    print(f'Y la lista completa es: \n{palabras}')
else:
    print(f'Con la letra {user} no hay ninguna palabra en la lista: \n{palabras}')