###
# Ejercicio 1: Operaciones básicas
# 📌 Pide dos números al usuario y muestra: suma, resta, multiplicación y división.
# (Reto extra: maneja el caso de división entre 0.)

import os       # importar el modulo os para limpiar la consola
os.system("cls")     # limpiar la consola (windows), en linux usar "clear"

print("\nEjercicio 1: Operaciones básicas")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
singo = input("Ingresa la operación (+, -, *, /): ")

if singo == "+":
    print(f"La suma de {num1} + {num2} es: {num1 + num2}")
elif singo == "-":
    print(f"La resta de {num1} - {num2} es: {num1 - num2}")
elif singo == "*":
    print(f"La multiplicación de {num1} * {num2} es: {num1 * num2}")
elif singo == "/":
    if num2 != 0:
        print(f"La división de {num1} / {num2} es: {num1 / num2}")
    else:
        print("Error: División entre 0 no está definida.")



###
# Ejercicio 2: Número par o impar
# 📌 Pide un número y dile al usuario si es par o impar.

print("\nEjercicio 2: Numero par")
num_par = float(input("Ingrese el numero que desa saber si es par o inpar: "))

par = num_par % 2

if par != 0:
    print(f"El numero {num_par}, es un numero impar")
else:
    print(f"El numero {num_par}, es un numero par")


###
# Ejercicio 3: Edad Futura
# 📌 Pide el nombre y la edad del usuario. Muestra un mensaje diciendo cuántos años tendrá en el 2050.

print("\nEjercicio 3: Edad futura")

edad = int(input("Ingrese su edad actual: "))

edad_futura = edad + 50

print(f"Dentro de 50 años vas a tener {edad_futura}")


###
# Ejercicio 4: El mayor de 3 numeros
# 📌 Pide tres números y muestra cuál es el mayor.
# (Reto extra: también cuál es el menor.)

print("\nEjercicio 4: Numero mayor")

num3 = float(input("ingresa un primer numero: "))
num4 = float(input("Ingresa un segundo numero: "))
num5 = float(input("Ingresa un tercer numero: "))

resultado1 = num3 - num4
resultado2 = num3 - num5
resultado3 = num4 - num5

if resultado1 > 0 and resultado2 > 0 and resultado3 > 0:
    print(f"En numero {num3}, es el mayory el numero {num5} es el menor, el tercer numero es {num4}")
elif resultado1 > 0 and resultado2 > 0 and resultado3 < 0:
    print(f"En numero {num3}, es el mayor y el numero {num4} es el menor, el tercer numero es {num5}")
elif resultado1 < 0 and resultado3 > 0 and resultado2 > 0:
    print(f"El numero {num4}, es el mayor y el numero {num5} es el menor, el tercer numero es {num3}")
elif resultado1 < 0 and resultado3 > 0 and resultado2 < 0:
    print(f"El numero {num4}, es el mayor y el numero {num3} es el menor, el tercer numero es {num5}")
elif resultado1 < 0 and resultado3 <0:
    print(f"El numero {num5}, es el mayor y el numero {num3} es el menor, el tercer numero es {num4}")
elif resultado1 > 0 and resultado3 <0:
    print(f"El numero {num5}, es el mayor y el numero {num4} es el menor, el tercer numero es {num3}")


###
# Ejercicio 5: Conversor de temperatura
# 📌 Pide una temperatura en grados Celsius y conviértela a Fahrenheit.
# 📌 Fórmula: F = C * 1.8 + 32

print("\nEjercicio 5: de Celcios a Fahrenheit")

grados = float(input("Introduce los grados Celcios que quieres pasar a grados Fahrenheit: "))

grados_F = (grados * 1.8 ) + 32

print(f"{grados}°C equivalen a {grados_F}°C")


###
# Ejercicio 6: Adivina el numero secreto 
# 📌 Guarda un número secreto en una variable.
# 📌 Pide al usuario que adivine el número.
# 📌 Si acierta → “¡Correcto!”, si no → “Intenta de nuevo”.
# (No uses ciclos todavía, solo un intento simple por ahora.)

print("\nEjercicio 6: Adivina el numero secreto")

intento_player = float(input("Adivina el codigo secreto introduciendo 4 numeros entre el 0 y el 9: "))

codigo = 3254

if codigo == intento_player:
    print("Lo tienes!! has adivinado el codig... felicitaciones")
else:
    print("Mejor suerte la proxima, vuelve a intertarlo")


###
# Ejercicio 7: Calculadora de propinas
# 📌 Pide el valor de una cuenta en un restaurante.
# 📌 Calcula el 10% como propina sugerida y muéstralo.

print("\nEjercicio 7: Calculadora de propinas para un restaurante")

cuenta = float(input("Introduce el valor de la cuenta para calcular el valor de la propina: "))

valor_propina = round(cuenta * 1.1, 2)

print(f"El valor de la cuenta con la propina incluida es de {valor_propina}")