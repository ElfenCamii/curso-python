###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

import os       # importar el modulo os para limpiar la consola
os.system("cls")     # limpiar la consola (windows), en linux usar "clear"

entrada1 = input("Introduce un número: ")
entrada2 = input("Introduce otro número: ")

try:
    num1 = float(entrada1)
    num2 = float(entrada2)
    print(f"El primer numero ingresado es {num1} y el segundo es {num2}")
except ValueError:
    print("¡Eso no es un número!")

# num1 = input("Introduce el primer número: ")
# num2 = input("Introduce el segundo número: ")

# num1 = float(num1)  # Convertir a float para permitir decimales
# num2 = float(num2) 


if num1 > num2:
    print(f"El número {num1} es mayor que {num2}.")
elif num2 > num1:
    print(f"El número {num2} es mayor que {num1}.")
else:
    print("Ambos números son iguales.") 


# Ejercicio 2: Verificar si un número es par o impar
# Pide al usuario que introduzca un número y muestra si es par o impar  

num = input("Introduce un número entero: ")
num = int(num)  # Convertir a entero

if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")


# Ejercicio 3: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

num1 = input("Introduce el primer número: ")
num2 = input("Introduce el segundo número: ")
operacion = input("Introduce la operación (+, -, *, /): ")
num1 = float(num1)  # Convertir a float para permitir decimales
num2 = float(num2)
resultado = None

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Error: La división por cero no esta permitida.")
else:
    print("Operación no válida.")
if resultado is not None:
    print(f"El resultado de {num1} {operacion} {num2} es {resultado}.") 


# Ejercicio 4: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

año = input("Introduce un año: ")
año = int(año)  # Convertir a entero
es_bisiesto = False
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    es_bisiesto = True  
if es_bisiesto:
    print(f"El año {año} es bisiesto.") 
else:
    print(f"El año {año} no es bisiesto.")      

# Ejercicio 5: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = input("Introduce una edad: ")
edad = int(edad) 
rango_edad = ""

if edad >= 65:
    rango_edad = "Adulto mayor"
elif edad >=18:
    rango_edad = "Adulto"
elif edad >=13:
    rango_edad = "Adolescente"
elif edad >=3:
    rango_edad = "Niño"
elif edad >=0:
    rango_edad = "Bebé"
print(f"La persona de {edad} años es un: {rango_edad}.")