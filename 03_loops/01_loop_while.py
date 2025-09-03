###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion
###

import os
os.system('cls')

print('\nBucle while')

# Bucle con una simple condición
contador = 0
while contador <= 5:
    print(contador)
    contador += 1   #La condición es super importante para evitar un bucle infinito


print('\nBucle while con break')
# Utilizando la palabra brak, para romper un bucle

contador = 0
while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle

# Ejemplo de bucle con break
print('\nContador decreciente de 100 que encuentra el primer multipo de 5')
contador = 100
while contador >= 0:
    contador -= 1
    print(contador)
    if contador % 5 == 0:
        print(f'El numero {contador} es multiplo de 5')
        break   #sale del bucle


# Continue, lo que hace es saltar esa interacción en concreto
# y continuar con el bucle
print('\nBucle con continue')
contador = 0
while contador < 10:
   contador += 1
   if contador % 2 == 0:
      continue
   print(contador)


# else, esta condición cuando se ejecuta?
print('\nBucle while con else:')
contador = 0
while contador < 5:
   print(contador)
   contador += 1
else:
   print('El bucle a terminado')


###
# Pedirle al usuario un número que tiene
# que ser positivo si no, no dejamos de pregutnar
###

# Modo simple
numero = -1 # Para tener un punto de partida
while numero <= 0:
   numero = int(input("Escribe un número positivo: "))
   if numero <= 0:
      print(f'El numero es {numero} y no es un numero positivo, intentalo nuevamente')

print(f'El número que has introducido es {numero}, el cual si es un número positivo, bien hecho!!!')

# Modo a prueba de fallos con TRY
numero = -1 # Para tener un punto de partida
while numero <= 0:
    try:
      numero = int(input("Escribe un número positivo: "))
      if numero <= 0:
        print(f'El numero es {numero} y no es un numero positivo, intentalo nuevamente')
    except:
      print("Lo que introduces debe de ser un número, que si no no funciona")

print(f'El número que has introducido es {numero}, el cual si es un número positivo, bien hecho!!!')

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# print("\nEjercicio 1:")

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
# print("\nEjercicio 3:")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
# print("\nEjercicio 6:")