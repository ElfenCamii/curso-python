# 🔥 EJERCICIO RETADOR FINAL

# Vas a crear un mini sistema de análisis.

# 🎯 Enunciado

# Pide al usuario 5 números y guárdalos en una lista.

# Después:

# Cuenta cuántos son pares
# Cuenta cuántos son impares
# Cuenta cuántos son mayores a 10

# Muestra:

# Lista completa
# Total pares
# Total impares
# Total mayores a 10

# BONUS:

# Si hay más pares que impares, muestra: "Hay más números pares"
# Si hay más impares que pares, muestra: "Hay más números impares"
# Si son iguales, muestra: "Hay la misma cantidad"

# 🔥 Condiciones

# No uses for
# Usa contadores manuales
# Usa condicionales
# Usa append()

# Sí se puede sin bucles.
# Te toca repetir inputs manualmente.

pares = 0
impares = 0
mayores_10 = 0
lista = []
lista_pares = []
lista_impares = []
lista_mas_10 = []

user_number_1 = int(input('Inserte el primer numero: '))
user_number_2 = int(input('Inserte el segundo numero: '))
user_number_3 = int(input('Inserte el tercer numero: '))
user_number_4 = int(input('Inserte el cuarto numero: '))
user_number_5 = int(input('Inserte el quinto numero: '))

lista.append(user_number_1)
lista.append(user_number_2)
lista.append(user_number_3)
lista.append(user_number_4)
lista.append(user_number_5)
print('La lista de numeros insertados es: ',lista)

if user_number_1 % 2 == 0:
    pares += 1
    lista_pares.append(user_number_1)
else:
    impares += 1
    lista_impares.append(user_number_1)

if user_number_2 % 2 == 0:
    pares += 1
    lista_pares.append(user_number_2)
else:
    impares += 1
    lista_impares.append(user_number_2)

if user_number_3 % 2 == 0:
    pares += 1
    lista_pares.append(user_number_3)
else:
    impares += 1
    lista_impares.append(user_number_3)

if user_number_4 % 2 == 0:
    pares += 1
    lista_pares.append(user_number_4)
else:
    impares += 1
    lista_impares.append(user_number_4)

if user_number_5 % 2 == 0:
    pares += 1
    lista_pares.append(user_number_5)
else:
    impares += 1
    lista_impares.append(user_number_5)

if user_number_1 >= 10:
    mayores_10 +=1
    lista_mas_10.append(user_number_1)

if user_number_2 >= 10:
    mayores_10 +=1
    lista_mas_10.append(user_number_2)

if user_number_3 >= 10:
    mayores_10 +=1
    lista_mas_10.append(user_number_3)

if user_number_4 >= 10:
    mayores_10 +=1
    lista_mas_10.append(user_number_4)

if user_number_5 >= 10:
    mayores_10 +=1
    lista_mas_10.append(user_number_5)

print('El total de pares es: ', pares, '\ny la lista es: ', lista_pares)
print('El total de impares es: ', impares, '\ny la lista es: ', lista_impares)
print('El total de numeros mayores a 10 es: ', mayores_10, '\ny la lista es: ', lista_mas_10)

if pares > impares:
    print('Hay más números pares')
elif pares < impares:
    print('Hay más números impares')
else:
    print('Hay la misma cantidad')