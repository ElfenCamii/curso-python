import os
os.system('cls')

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.

print("\nEjercicio 1: Cuenta inversa")

contador = 10

while contador >= 0:
    print(contador)
    contador -= 1


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.

print("\nEjercicio 2: Suma de numeros pares")

numero = 1
suma_pares = 0

while numero <= 20:
    numero += 1
    if numero % 2 == 0:
        suma_pares += numero

print(f"La suma de los números pares hasta 20 es: {suma_pares}")


# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

# Funciona pero no del todo
print("\nEjercicio 3: Factorial de un número")

num_user = int(input('Introduce un numero entero positivo: '))
factorial = num_user

while factorial > 1:
    factorial -= 1 
    num_user *= factorial

print(f"El factorial es: {num_user}")

# # Funciona del todo
print("\nEjercicio 3:")

numero = int(input("Introduce un número entero positivo: "))
factorial = 1
contador = 1

while contador <= numero:
  factorial *= contador
  contador += 1

print(f"El factorial de {numero} es: {factorial}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".

print("\nEjercicio 4: Validación de contraseña")

user = " "
password = "holimundo"

while user != password:
    user = input('introduce la contraseña para ingresar: ')
    if user != password:
        print("contraseña incorrecta intentalo nuevamente")
print('Lo hiciste!!! Contraseña correcta')


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.

print("\nEjercicio 5: Tabla de multiplicar")

numero_usuario = int(input('Introduce el numero del que quieres saber la tabla de multiplicar: '))
multiplicador = 0

print(f'La tabal de multiplicar de {numero_usuario} es:')

while multiplicador < 10:
    multiplicador += 1
    print(multiplicador * numero_usuario)


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

# print("\nEjercicio 6: Números primos hasta N")

# user_number = int(input('Introduce un numero entero positivo: '))
# num_primo = 0
# comprobante = 0

# while num_primo <= user_number:
#     num_primo += 1
#     comprobante =+ 1
#     if num_primo % 1 == 0 and num_primo % comprobante == 0:
#         print(num_primo)

#     print('no entro al if')

print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1