###
# Juego 1: Numero secreto
# Crea un programa en el que el usuario introduzca números enteros entre 0 y 100
# Hasta adivinar un numero secreto dado por la libreria random
# El programa debe avisar si el número introducido por el usuario es más grande o más pequeño
###

import os
import random as rnd

while True: 
    os.system('cls')
    print('🤫🤫 Juego del número secreto 🤐🤐')
    print('''
        1: Fácil 😴
        2: Normal 😏
        3: Imposible 🤯''')
    dif_game = int(input('\nElige la dificultad del juego: '))

    if dif_game == 1:
        print('\nBienvenido a la dificultad Fácil 😴')
        print('Tendras que adivinar el numero secreto entre 1 y 50')
        num_random = rnd.randint(1, 50)
        num_try = 0
        numbers_user = []

        while True:
            num_user = int(input('\nIngresa tu número (entre 1 a 50): '))
            num_try += 1
            if num_user == num_random: break
            elif num_user > num_random:
                if (num_user - num_random) <= 2: print('🔥🔥🔥 Estas que te quemas 🔥🔥🔥. Elije un número menor!')
                elif (num_user - num_random) <= 8: print('🔥 Estas caliente 🔥. Elije un número menor!')
                elif (num_user - num_random) <= 16: print('🥵 Estas tibio 🥵. Elije un número menor!')
                elif (num_user - num_random) <= 24: print('🥶 Estas frio 🥶. Elije un número menor!')
                elif (num_user - num_random) <= 30: print('☃️ Estas helado ☃️. Elije un número menor!')
                elif (num_user - num_random) <= 50: print('☃️☃️ Te congelaste ☃️☃️. Elije un número menor!')
            else: 
                if (num_random - num_user) <= 2: print('🔥🔥🔥 Estas que te quemas 🔥🔥🔥. Elije un número mayor!')
                elif (num_random - num_user) <= 8: print('🔥 Estas caliente 🔥. Elije un número mayor!')
                elif (num_random - num_user) <= 16: print('🥵 Estas tibio 🥵. Elije un número mayor!')
                elif (num_random - num_user) <= 24: print('🥶 Estas frio 🥶. Elije un número mayor!')
                elif (num_random - num_user) <= 30: print('☃️ Estas helado ☃️. Elije un número mayor!')
                elif (num_random - num_user) <= 50: print('☃️☃️ Te congelaste ☃️☃️. Elije un número mayor!')
            numbers_user.append(num_user)
        print(f'🎊🎉elicitaciones🎉🎊. Adivina el numero secreto en tan solo {num_try} intentos')
        print(f'Los numeros que usaste son los siguientes: \n{numbers_user}')
    elif dif_game == 2:
        print('\nBienvenido a la dificultad Normal 😏')
        print('Tendras que adivinar el numero secreto entre 1 y 100')
        num_random = rnd.randint(1, 100)
        num_try = 0
        numbers_user = []

        while True:
            num_user = int(input('\nIngresa tu número (entre 1 a 100): '))
            num_try += 1
            if num_user == num_random: break
            elif num_user > num_random:
                if (num_user - num_random) <= 3: print('🔥🔥🔥 Estas que te quemas 🔥🔥🔥. Elije un número menor!')
                elif (num_user - num_random) <= 10: print('🔥 Estas caliente 🔥. Elije un número menor!')
                elif (num_user - num_random) <= 20: print('🥵 Estas tibio 🥵. Elije un número menor!')
                elif (num_user - num_random) <= 30: print('🥶 Estas frio 🥶. Elije un número menor!')
                elif (num_user - num_random) <= 40: print('☃️ Estas helado ☃️. Elije un número menor!')
                elif (num_user - num_random) <= 100: print('☃️☃️ Te congelaste ☃️☃️. Elije un número menor!')
            else: 
                if (num_random - num_user) <= 3: print('🔥🔥🔥 Estas que te quemas 🔥🔥🔥. Elije un número mayor!')
                elif (num_random - num_user) <= 10: print('🔥 Estas caliente 🔥. Elije un número mayor!')
                elif (num_random - num_user) <= 20: print('🥵 Estas tibio 🥵. Elije un número mayor!')
                elif (num_random - num_user) <= 30: print('🥶 Estas frio 🥶. Elije un número mayor!')
                elif (num_random - num_user) <= 40: print('☃️ Estas helado ☃️. Elije un número mayor!')
                elif (num_random - num_user) <= 100: print('☃️☃️ Te congelaste ☃️☃️. Elije un número mayor!')
            numbers_user.append(num_user)
        print(f'🎊🎉elicitaciones🎉🎊. Adivina el numero secreto en tan solo {num_try} intentos')
        print(f'Los numeros que usaste son los siguientes: \n{numbers_user}')
    elif dif_game == 3:
        print('\nBienvenido a la dificultad Imposible 🤯')
        print('Tendras que adivinar el numero secreto entre 1 y 100 en solo 5 intentos 😮😮')
        num_random = rnd.randint(1, 100)
        num_try = 0
        numbers_user = []

        while num_try < 5:  # máximo 5 intentos
            num_user = int(input('\nIngresa tu número (entre 1 a 100): '))
            num_try += 1
            numbers_user.append(num_user)
            guessed = False
            if num_user == num_random:
                guessed = True
                break
            elif num_user > num_random:
                if (num_user - num_random) <= 3: print('🔥🔥🔥 Estas que te quemas 🔥🔥🔥. Elije un número menor!')
                elif (num_user - num_random) <= 10: print('🔥 Estas caliente 🔥. Elije un número menor!')
                elif (num_user - num_random) <= 20: print('🥵 Estas tibio 🥵. Elije un número menor!')
                elif (num_user - num_random) <= 30: print('🥶 Estas frio 🥶. Elije un número menor!')
                elif (num_user - num_random) <= 40: print('☃️ Estas helado ☃️. Elije un número menor!')
                elif (num_user - num_random) <= 100: print('☃️☃️ Te congelaste ☃️☃️. Elije un número menor!')
            else: 
                if (num_random - num_user) <= 3: print('🔥🔥🔥 Estas que te quemas 🔥🔥🔥. Elije un número mayor!')
                elif (num_random - num_user) <= 10: print('🔥 Estas caliente 🔥. Elije un número mayor!')
                elif (num_random - num_user) <= 20: print('🥵 Estas tibio 🥵. Elije un número mayor!')
                elif (num_random - num_user) <= 30: print('🥶 Estas frio 🥶. Elije un número mayor!')
                elif (num_random - num_user) <= 40: print('☃️ stas helado ☃️. Elije un número mayor!')
                elif (num_random - num_user) <= 100: print('☃️☃️ Te congelaste ☃️☃️. Elije un número mayor!')
            numbers_user.append(num_user)
        if guessed == True:
            print(f'\n🎊🎉 Felicitaciones 🎉🎊. Adivinaste el número secreto en {num_try} intentos')
            print(f'Los números que usaste son: {numbers_user}')
        else:
            print(f'\n😢 Lo siento, te quedaste sin intentos. El número era {num_random}')
            print(f'Tus intentos fueron: {numbers_user}')
    play_again = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if play_again != "s":
        print("\nGracias por jugar. ¡Hasta pronto! 👋")
        break