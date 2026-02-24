# 1️⃣ Mayor, menor o igual

# Crea dos variables:
# a = 10
# b = 20
# Imprime:
# “a es mayor que b”
# “a es menor que b”
# “a es igual a b”

a = int(input('Escribe un numero para evaluar: '))
b = int(input('Escribe un segundo numero a evaluar: '))

if a > b:
    print(f'El numero {a} es mayor que el numero {b}')
elif a < b:
    print(f'El numero {a} es menor que el numero {b}')
else:
    print(f'El numero {a} es igual que el numero {b}')

# 2️⃣ Número positivo, negativo o cero

# Dado un número:
# num = -5
# Determina si es:
# positivo
# negativo
# o cero

num = int(input('Escribe un numero entero: '))

if num > 0:
    print(f'El numero {num} es mayor que 0')
elif num < 0:
    print(f'El numero {num} es menor que 0')
else:
    print(f'El numero es 0')

# 3️⃣ Número par o impar

# Dado:
# numero = 13
# Imprime si es:
# par
# impar

dado = int(input('Escribe el numero que desees saber si es par: '))
dado_abs = abs(dado)

if dado_abs % 2 == 0:
    print(f'El numero {dado} es un numero par')
else:
    print(f'El numero {dado} es un numero impar')

# 4️⃣ Mayor de edad con mensaje personalizado

# Pide al usuario su edad.
# Imprime:
# “Eres menor de edad”
# “Eres mayor de edad”
# “Eres adulto mayor” (si tiene más de 65)

age = int(input('Escribe tu edad: '))

if age >= 65:
    print(f'Tienes {age} añor, eres un adulto mayor')
elif age >= 18:
    print(f'Tienes {age} años, eres mayor de edad')
else:
    print(f'Tienes {age} años, eres menor de edad')

# Define una contraseña:

# password_real = "python123"
# Pide al usuario una contraseña e imprime:
# “Acceso concedido”
# “Acceso denegado”

password_real = 'python123'
password_user = input("Ingresa la contraseña: ")

if password_user == password_real:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# 6️⃣ Comparación de strings

# Dado:
# lenguaje = "Python"
# Verifica si el usuario escribió:
# "python"
# "PYTHON"
# "Python"
# 👉 sin importar mayúsculas/minúsculas

palabra = 'Python'
palabra_user = input('Escribe la palabra: ')

if palabra_user == 'python':
    print('La palabra ingresada fue python')
elif palabra_user == 'PYTHON':
    print('La palabra ingresada fue PYTHON')
elif palabra_user == 'Python':
    print('La palabra ingresada fue PYTHON')
else:
    print('La palabra no tiene nada que ver con Python')

# 7️⃣ Clasificación de notas

# Dado:
# nota = 3.7
# Imprime:
# “Reprobado” (< 3.0)
# “Aprobado” (3.0 a 4.5)
# “Excelente” (> 4.5)

nota = float(input('Ingrese la nota del estudiante: '))

if 5 >= nota >= 4.5:
    print(f'La nota fue {nota}, Excelente, sigue así')
elif 4.5 > nota >= 3:
    print(f'La nota fue {nota}, Aporobado, aun puede mejorar')
elif 3 > nota >= 0:
    print(f'La nota fue {nota}, Reprobado, a estudiar más')
else:
    print(f'La nota {nota}, esta fuera de los rangos de calificación')

# 8️⃣ Verificación múltiple (AND)

# Dado:
# edad = 25
# tiene_cedula = True
# Imprime:
# “Puede votar” si cumple ambas condiciones
# “No puede votar” si no

edad = int(input('Escriba su edad:'))
tiene_id = input('Escriba "si" o "no" si cuenta con cedula: ')
tiene_id = tiene_id.lower()

if edad >= 18 and tiene_id == 'si':
    print(f'ya que tenes {edad} años y tienes cedula, puedes votar')
elif edad >= 18 and tiene_id == 'no':
    print(f'Aunque tienes {edad} años, al no tener cedula no puedes votar')
elif edad < 18 and tiene_id == 'si':
    print('Como tienes {edad} años y tienes cedula, vamos a llamar a la policia por que es ilegal')
else:
    print('No puedes votar')

# 9️⃣ Verificación múltiple (OR)

# Dado:
# tiene_descuento = False
# es_estudiante = True
# Imprime:
# “Aplica descuento” si al menos una es True
# “No aplica descuento” si ambas son False

tiene_descuento = input('Tiene descuento? (si/no): ').lower() == 'si'
es_estudiante = input('Es estudiante? (si/no): ').lower() == 'si'

if tiene_descuento or es_estudiante:
    print('Aplica descuento')
else:
    print('No aplica descuento')

# 🔟 Comparación de tres números

# Dado:
# x = 5
# y = 9
# z = 3
# Determina cuál es el mayor de los tres.

x = int(input('Ingrese un numero entero: '))
y = int(input('Ingrese un numero entero: '))
z = int(input('Ingrese un numero entero: '))

if x - y >= 0 and x - z > 0:
    print(f'El numero mayor es {x}')
elif x - y >= 0 and x - z < 0:
    print(f'El numero mayor es {z}')
elif x - y < 0 and y - z >= 0:
    print(f'El numero mayor es {y}')
else:
    print(f'El numero mayor es {z}')


# otra solucion:

x = int(input('Ingrese un numero entero: '))
y = int(input('Ingrese un numero entero: '))
z = int(input('Ingrese un numero entero: '))

mayor = x

if y > mayor:
    mayor = y
if z > mayor:
    mayor = z

print(f'El número mayor es {mayor}')

# 🧩 BONUS (reto extra 🔥)

# Haz un programa que:
# pida un número
# diga si es par
# diga si es positivo
# diga si es mayor que 100
# 👉 todo en un solo programa

guess_number = int(input('Ingrese un numero entero, puede ser positivo o negativo: '))

if guess_number >= 100 and guess_number % 2 == 0:
    print(f'El numero {guess_number} es mayor que 100 y es par')
elif guess_number >= 100 and guess_number % 2 == 1:
    print(f'El numero {guess_number} es mayor que 100 y es impar')
elif guess_number >= 0 and guess_number % 2 == 0:
    print(f'El numero {guess_number} es positivo y es par')
elif guess_number >= 0 and guess_number % 2 == 1:
    print(f'El numero {guess_number} es positivo y es impar')
elif guess_number <= 0 and guess_number % 2 == 0:
    print(f'El numero {guess_number} es negativo y es par')
else:
    print(f'El numero {guess_number} es negativo y es impar')

### Otra solución

guess_number2 = int(input('Introduce un numero entero, puede ser positivo o negativo '))

if guess_number2 % 2 == 0:
    print(f'El numero {guess_number2} es par')
else:
    print(f'El numero {guess_number2} es impar')

if guess_number2 > 0:
    print(f'El numero {guess_number2} es positivo')
elif guess_number2 < 0: 
    print(f'El numero {guess_number2} es negativo')
else:
    print('El numero es 0')

if guess_number2 > 100:
    print(f'El numero {guess_number2} es mayor que 100')
else:
    print('El numero es menor que 100')