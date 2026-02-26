# 🔥 EJERCICIO ÚNICO – MODO PRUEBA TÉCNICA

# ⏱ Tiempo máximo: 30 minutos
# 📊 Nivel: Junior Backend Inicial
# 🧠 Consolida:

# while

# contador
# acumulador
# validación
# múltiples condiciones de salida
# control limpio de flujo

# 🎯 Enunciado – Sistema de Control de Acceso Numérico

# Crea un sistema que:
# Tenga un número secreto = 15
# Permita máximo 5 intentos
# En cada intento:
# Pida un número
# Si no es número → no contar el intento
# Si es negativo → no contar el intento
# Si el número es correcto:
# Mostrar en qué intento acertó
# Terminar

# Si el número es mayor:
# Mostrar “Demasiado alto”
# Si es menor:
# Mostrar “Demasiado bajo”
# Si se agotan los 5 intentos:
# Mostrar “Intentos agotados”
# Permitir escribir "salir" en cualquier momento

import os
os.system('cls')

secret_number = 15
count = 5
numbers = []

while count > 0:
    print('Adivina el numero secreto!!\n')
    print(f'Ojo solo tienes {count} intentos')
    print('Puedes escribir salir en cualquier momento para terminar el juego')
    user_number = (input('Ingrea el numero que pienses que es: '))
    if user_number.lower() != 'salir':
        try:
            number_user = int(user_number)
            if number_user < 0:
                print('El numero tiene que ser positivo\n')
            elif number_user > secret_number:
                print('\nEl numero es demasiado alto\n')
                numbers.append(number_user)
                count -= 1
            elif number_user < secret_number:
                print('\nEl numero es demasiado Bajo\n')
                numbers.append(number_user)
                count -= 1
            else:
                numbers.append(number_user)
                print(f'\nLo tienes {user_number} era el numero muy bien')
                print(f'Lo lograste en el {6 - count} intento')
                print(f'Los numeros usados fueron {numbers}')
                break
        except ValueError:
            print('\nEl valor ingresado no es valido!\n')
    else:
        print(f'Los numeros que usaste fueron {numbers}')
        print('\nHasta la proxima!!')
        break

if count == 0:
    print('Perdiste')
    print('Te quedaste sin intento mas suerte para la poxima')
    print(f'Los numeros que usaste fueron {numbers}')


###
# Otro tipo de errores con try/ except
###

# ValueError → valor incorrecto
# TypeError → tipo de dato incorrecto
# ZeroDivisionError → dividir por cero
# IndexError → índice fuera de rango