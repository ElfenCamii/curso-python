# 🏆 BONUS – Simulación tipo prueba técnica

# ⏱ Tiempo máximo: 25 minutos
# 📊 Nivel: Junior real

# Enunciado

# Crea un programa que:
# Pida un número entero positivo N.
# Calcule la suma de todos los números pares entre 1 y N.
# Calcule la suma de todos los números impares entre 1 y N.
# Muestre cuál suma es mayor.
# Si son iguales, indicarlo.
# Validar que N sea positivo.
# Si no es válido, volver a pedirlo.

import os 
os.system('cls')

while True:

    pares = 0
    impares = 0
    suma_pares = 0
    suma_impares = 0

    jugar = input('Escriba si/no si decea averiguar un numero: ').lower()
    if jugar == 'si':
        try:
            user_number = int(input('Escriba un numero entero positivo: '))
            if user_number <= 0:
                    print('El numero tiene que ser positivo mayor que 0')
            else:
                for n in range(1, user_number + 1):
                    if n % 2 == 0:
                        pares += 1
                        suma_pares += n            
                    else:
                        impares += 1
                        suma_impares += n
                        
                print('Total de numero pares pares: ',pares)
                print('La suma de los numero pares es:', suma_pares)
                print('Total de numeros impares: ',impares)
                print('La suma de los numeros impares es: ', suma_impares)
                if suma_pares > suma_impares:
                    print('La suma de los pares es mayor')
                elif suma_pares < suma_impares:
                    print('La suma de los impares es mayor')
                else:
                    print('La suma de ambos es igual')
        except ValueError:
            print('El valor ingresado no es valido')
    else:
        print('Gracias hasta la proxima!')
        break

###
# Solucion de GPT como si fuera un junior
###

while True:
    jugar = input('¿Desea ingresar un numero? (si/no): ').lower()

    if jugar == 'no':
        print('Gracias hasta la proxima!')
        break

    if jugar != 'si':
        print('Opcion invalida')
        continue

    try:
        user_number = int(input('Escriba un numero entero positivo: '))

        if user_number <= 0:
            print('El numero debe ser mayor que 0')
            continue

        pares = 0
        impares = 0
        suma_pares = 0
        suma_impares = 0

        for n in range(1, user_number + 1):
            if n % 2 == 0:
                pares += 1
                suma_pares += n
            else:
                impares += 1
                suma_impares += n

        print('Total de numeros pares:', pares)
        print('Suma de pares:', suma_pares)
        print('Total de numeros impares:', impares)
        print('Suma de impares:', suma_impares)

        if suma_pares > suma_impares:
            print('La suma de los pares es mayor')
        elif suma_impares > suma_pares:
            print('La suma de los impares es mayor')
        else:
            print('Ambas sumas son iguales')

    except ValueError:
        print('El valor ingresado no es valido')