import os
os.system('cls')

# 🔹 1️⃣ Contador básico

# Imprime los números del 1 al 10 usando while.

contador = 1
while contador <= 10:
    print(contador)
    contador += 1

# 🔹 2️⃣ Contador descendente

# Imprime del 10 al 1 usando while.

contador = 10
while contador >= 1:
    print(contador)
    contador -= 1

# 🔹 3️⃣ Suma acumulada

# Pide al usuario un número n.
# Usando while, calcula la suma desde 1 hasta n.

# Ejemplo:
# Si el usuario pone 5 → resultado 15.

suma = 0
contador = 0
user = int(input('Escribe en numero del que desees saber las sumas: '))

while contador <= user:
    suma += contador
    contador += 1

print(suma)

# 🔹 4️⃣ Contar pares

# Pide un número n.
# Cuenta cuántos números pares hay desde 1 hasta n.

contador = 1
pares = 0
user = int(input('Escribe un numero entero positivo: '))

while contador <= user:
    if contador % 2 == 0:
        pares += 1
    contador += 1
print(pares)

# 🔹 5️⃣ Validación de contraseña

# Define una contraseña correcta (por ejemplo "python123").
# Pide al usuario que la escriba.
# Mientras sea incorrecta, vuelve a pedirla.
# Cuando la escriba bien, muestra:
# "Acceso concedido".

password = 'python123'
contador = 5

while True:
    user_passrod = input('Ingrese la contraseña: ')
    if password == user_passrod:
        print('Contraseña correcta, puedes ingresar')
        break
    else:
        contador -= 1
        if contador >= 1:
            print('Contraseña incorrecta, intente de nuevo')
            print('Numero de intentos disponibles:', contador)
        else:
            contador = 0
            print('Te quedaste sin intentos')
            print('Mentiras tienes intentos infinitos')
            
print('Numero de intentos restantes:', contador)


# 🔹 6️⃣ Menú repetitivo simple

# Crea una lista vacía.

# Usando while, muestra un menú:
# Agregar número
# Mostrar lista
# Salir

# El programa debe repetirse hasta que el usuario elija salir.

lista_numeros = []
print('''
Escriba el numero del menu segun la acción que desee      

1. Agregar numero
2. Mostrar lista
3. Salir
''')

while True:
    user_action = int(input('Digite en numero de la acción que desea realizar: '))
    if user_action == 1:
        user_number = int(input('Escriba el numero entero que desee agregar a la lista: '))
        lista_numeros.append(user_number)
    elif user_action == 2:
        print(lista_numeros)
    elif user_action == 3:
        break
print('Gracias, hasta la proxima')

# 🔹 7️⃣ Adivinar el número

# Define un número secreto (ej: 7).
# Mientras el usuario no lo adivine:
# Pide un número
# Di si es mayor o menor que el secreto

secret_number = 8

while True:
    user_try = int(input('Ingrese un numero del 0 al 10: '))
    if user_try > secret_number:
        print(f'El numero {user_try} es mayor que el numero a adivinar')
    elif user_try < secret_number:
        print(f'El numero {user_try} es menor que el numero a adivinar')
    elif user_try == secret_number:
        break
print(f'Felicidades el numero {user_try} era el numero a adivinar')