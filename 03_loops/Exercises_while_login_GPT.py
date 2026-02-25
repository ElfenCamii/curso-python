# 🔥 EJERCICIO 2 – Sistema de Login con Bloqueo

# Simula un sistema donde:
# Usuario correcto: "admin"
# Contraseña correcta: "1234"
# Máximo 3 intentos

# Si falla 3 veces → mostrar “Cuenta bloqueada”
# Si acierta → “Bienvenido” y termina
# Si escribe "salir" en cualquier momento → termina

# Aquí entrenas:
# ✔ contador de intentos
# ✔ múltiples condiciones de salida
# ✔ lógica de seguridad básica

import os
os.system('cls')

usuario = 'admin'
password = '1234'
password_trys = 3

while password_trys > 0:

    print('Bienvenido a Facecamii')
    print('Para ingresar llene sus credenciales, para salir, escriba la palabra "salir" en cualquier momento')

    user_usuario = input('Ingresee su nombre de usuario: \n')
    if user_usuario.lower() != 'salir':
        print('Usuario ingresado con exito')
    else:
        print('Hasta la proxima!')
        break
    user_password = input('Ingrese su coontraseña \n')
    if user_password.lower() != 'salir':
        print('Contraseña ingresada con exito')
    else:
        print('Hasta la proxima!')
        break

    if user_usuario != usuario or user_password != password:
        password_trys -= 1
        print(f'\nNombre de usuario o contraseña incorrectos \nNumero de intentos restantes: {password_trys}\n')
    else:
        print(f'Bienvenido! {user_usuario}')
        break

if password_trys == 0:
    print('Cuenta bloqueada!')