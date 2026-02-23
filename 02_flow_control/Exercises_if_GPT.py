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