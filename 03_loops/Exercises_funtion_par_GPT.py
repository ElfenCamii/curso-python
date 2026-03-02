# 🟣 🔥 Reto para empezar mañana

# 7️⃣ Función que cuente pares en una lista

# Debe:

# Recibir una lista de números.
# Usar la función par() que ya creaste.
# Contar cuántos números de la lista son pares.
# Retornar el total.
# No imprimir dentro de la función.

# Ejemplo esperado

# Si la lista es:

# [3, 4, 7, 10, 11, 8]

# Debe retornar:

# 3

# Porque los pares son: 4, 10, 8.

import os
os.system('cls')

def par(a):
    return a % 2 == 0

def bienvenida():
    print('Bienveniodo a conteo de pares')

lista = []
lista_pares = []
bienvenida()
while True:
    add_number = input('Desea agregar un numero a la lista si/no: \n').lower()
    if add_number == 'si':
        try:
            user = int(input('Ingrese un numero para la lista: '))
            lista.append(user)
            if par(user):
                lista_pares.append(user)
        except ValueError:
            print('El valor ingresado no es un numero')
    elif add_number == 'no':
        print('La lista completa fue: \n',lista)
        print('La lista de pares fue: \n', lista_pares)
        print('El total de pares fue: \n', len(lista_pares))
        break
    else:
        print('Texto ingresado no valido')