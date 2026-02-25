# 🔥 EJERCICIO 1 – Simulación de Cajero (nivel intermedio)

# Crea un sistema que:

# Empiece con saldo = 1000
# Muestre un menú repetitivo:
# Consultar saldo
# Depositar dinero
# Retirar dinero
# Salir

# No permita retirar más de lo que hay
# No permita ingresar números negativos
# Termine solo cuando el usuario elija salir

# Aquí entrenas:
# ✔ control de estado
# ✔ validaciones
# ✔ múltiples decisiones
# ✔ bucle principal tipo sistema real

import os
os.system('cls')

saldo = 1000

while True:
    print('''
Bienvenido al Cajero del Banco Camiibank
Que decea hacer hoy:
             
1. consultar saldo
2. Depositar dinero
3. Retirar dinero
4. Salir
''')
    user_acction = input('Introduce el número de la acción que deceas hacer o escribe "Salir" o 4 para terminar la transapción: ')
    if user_acction == '1':
        print(f'\nEl saldo disponeble es: ${saldo}')
    elif user_acction == '2':
        try:
            deposito = int(input('Ingrese el monto que desea depositar: '))
            if deposito > 0:
                confirmacion = input(f'Esta seguro que decea realizar un deposito de ${deposito}? \n si/no: ').lower()
                while True:
                    if confirmacion == 'si':
                        saldo += deposito
                        print('\nDeposito realizado con exito!')
                        break
                    elif confirmacion == 'no':
                        print('El deposito ha sido cancelado')
                        break
                    else:
                        print('La respuesta no es valida')
                        break
            else:
                print('\nEl valor ingresado no es valido para el deposito')
        except:
            print('\nEl valor ingreesado no es un numero!')
    elif user_acction == '3':
        try:
            retiro = int(input('Ingrese el monto que desea retirar: '))
            if retiro <= saldo and retiro > 0:
                confirmacion = input(f'Esta seguro que decea realizar un retiro de ${retiro}? \n si/no: ').lower()
                while True:
                    if confirmacion == 'si':
                        saldo -= retiro
                        print('\nRetiro ha sido realizado con exito!')
                        break
                    elif confirmacion == 'no':
                        print('El retiro ha sido cancelado')
                        break
                    else:
                        print('La respuesta no es valida')
                        break
            elif retiro > saldo and retiro > 0:
                print('\nEl valor a retirar supera su saldo actual')
            else:
                print('\nEl monto a retirar no es valido')
        except:
            print('\nEl valor ingresado no es un numero!')
    elif user_acction.lower() == 'salir' or user_acction == '4':
        break

print('\nGracias por visitarnos, que tenga buen día.')