###
# 01 - sentencias condicionales (if, elif, else)
# permiten ejecutar bloques de codigo solo si se cumplen ciertas condiciones
###

import os       # importar el modulo os para limpiar la consola
os.system("cls")     # limpiar la consola (windows), en linux usar "clear"

print("\n Sentencia simple condicional if")

edad = 18

if edad >= 18:
    print(f"tienes {edad}, Eres mayor de edad")
    print("Puedes votar")

print("\n Sentencia compuesta condicional else")
edad = 16

if edad < 18:
    print(f"tienes {edad}, Eres menor de edad")
    print("No puedes votar")
else:
    print(f"Tienes {edad}, Eres mayor de edad")
    print("Puedes votar")

print("\n Sentencia condicional multiple elif")

nota = 4
if nota >= 9:
    print(f"tu nota fue {nota}, Sobresaliente")
elif nota >= 7:
    print(f"tu nota fue {nota},Notable")
elif nota >= 5:
    print(f"tu nota fue {nota},Aprobado")
else:
    print(f"tu nota fue {nota},reprobado")


#javaScript
#and -> &&
#or  -> ||  
#not -> !

print("\n condiciones multiples")

edad = 15
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir")

if edad >= 18 or tiene_licencia:
    print("Puedes conducir bajo ciertas condiciones")
else:
    print("No puedes conducir a menos que tengas 18 años o licencia")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Es dia de semana, a trabajar!")


numero = 7
if numero: #True
    print("El numero no es cero")

numero = 0
if numero: #False
    print("Aca no entra nunca porque es cero")

nombre = "Juan"
if nombre: #True
    print("El nombre no es una cadena vacia")

numero =3
es_el_tres = (numero == 3)

if es_el_tres:
    print("El numero es tres")

print("\n La condicion terniaria")
# es una forma concisa de un if-else en una linea de codigo
# [codigo si se cumple la dondicion] if [condicion] else [codigo si no se cumple la condicion]

edad = 18
mensaje = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad" 
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)