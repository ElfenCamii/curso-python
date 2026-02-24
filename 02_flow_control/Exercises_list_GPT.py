import os
os.system ('cls')

# 1️⃣ Acceder a posiciones específicas
# numeros = [10, 20, 30, 40, 50]

# Imprime:
# el primer número
# el segundo número
# el último número

list1 = [10, 20, 30, 40, 50]

print('El primer elemento de la lista es: \n', list1[0])
print('El segundo elemento de la lista es: \n', list1[1])
print('El ultimo elemento de la lista es: \n', list1[-1])

# 2️⃣ Longitud de la lista
# colores = ["rojo", "azul", "verde", "amarillo"]

# Imprime cuántos elementos tiene la lista usando len()

list_colores = ["rojo", "azul", "verde", "amarillo"]

print('La longitud de la lista es: \n', len(list_colores))

# 3️⃣ Suma manual de 3 elementos
# numeros = [5, 8, 12]

# Suma los 3 valores accediendo por índice (sin ciclos)

list_numeros = [5, 8, 12]
suma_list = list_numeros[0] + list_numeros[1] + list_numeros[2]

print('La suma de los numeros de la lista es: \n', suma_list)

# 4️⃣ Comparar elementos
# numeros = [4, 9]

# Usa if para imprimir cuál número es mayor

list_mayor = [4, 9]

if list_mayor[0] > list_mayor[1]:
    print(f'El numero {list_mayor[0]} es mayor que {list_mayor[1]}')
elif list_mayor[0] == list_mayor[1]:
    print('Los dos numeros son iguales')
else:
    print(f'El numero {list_mayor[1]} es mayo que {list_mayor[0]}')

# 5️⃣ Par o impar en lista
# numeros = [7, 10, 13]

# Imprime si cada uno es par o impar (uno por uno usando índice)

par_numeros = [7, 10, 13]

if par_numeros[0] % 2 == 0:
    print(f'El numero {par_numeros[0]} es par')
else:
    print(f'El numero {par_numeros[0]} es impar')

if par_numeros[1] % 2 == 0:
    print(f'El numero {par_numeros[1]} es par')
else:
    print(f'El numero {par_numeros[1]} es impar')

if par_numeros[2] % 2 == 0:
    print(f'El numero {par_numeros[2]} es par')
else:
    print(f'El numero {par_numeros[2]} es impar')

# 6️⃣ Positivo o negativo
# numeros = [-5, 3, 0]

# Imprime para cada número si es:
# positivo
# negativo
# cero

lista_numeros = [-5, 3, 0]

if lista_numeros[0] == 0:
    print(f'El numero es 0')
elif lista_numeros[0] > 0:
    print(f'El numero {lista_numeros[0]} es positivo')
elif lista_numeros[0] < 0:
    print(f'El numero {lista_numeros[0]} es negativo')

if lista_numeros[1] == 0:
    print(f'El numero es 0')
elif lista_numeros[1] > 0:
    print(f'El numero {lista_numeros[1]} es positivo')
elif lista_numeros[1] < 0:
    print(f'El numero {list_numeros[1]} es negativo')

if lista_numeros[2] == 0:
    print(f'El numero es 0')
elif lista_numeros[2] > 0:
    print(f'El numero {lista_numeros[2]} es positivo')
elif lista_numeros[2] < 0:
    print(f'El numero {lista_numeros[2]} es negativo')

# 7️⃣ Lista de nombres en mayúscula
# nombres = ["camilo", "ana", "luis"]

# Imprime cada nombre en mayúscula usando .upper()

list_nombres = ["camilo", "ana", "luis"]
nombres = [list_nombres[0].upper(), list_nombres[1].upper(), list_nombres[2].upper()]

print('Los nombres de la lista en mayusculas son: \n',nombres)

# 8️⃣ Verificar si un elemento coincide
# frutas = ["manzana", "pera", "uva"]

# Pide al usuario una fruta y verifica si es igual a:

# frutas[0]
# frutas[1]
# frutas[2]

# 👉 Usa if con or

frut_user = input('Ingresa una fruta: ')
list_fruts = ["manzana", "pera", "uva"]

if frut_user.lower() == list_fruts[0] or frut_user.lower() == list_fruts[1] or frut_user.lower() == list_fruts[2]:
    print('La fruta del usuario coincide con la lista y es: ')
    if frut_user.lower() == list_fruts[0]:
        print('Manzana')
    elif frut_user.lower() == list_fruts[1]:
        print('Pera')
    elif frut_user.lower() == list_fruts[2]:
        print('Uva')
else:
    print(f'La fruta {frut_user} no esta en la lista')

# 9️⃣ Comparar primero y último
# numeros = [15, 8, 22, 4]

# Imprime si el primero es mayor que el último

list_comparation = [15, 8, 22, 4]

if list_comparation[0] == list_comparation[-1]:
    print('El primer y ultimo numero de la lista son iguales')
elif list_comparation[0] > list_comparation[-1]:
    print(f'El primer numero de la lista es {list_comparation[0]} y es mayor que {list_comparation[-1]} que es el ultimo')
else:
    print(f'El primer numero de la lista es {list_comparation[0]} y es menor que {list_comparation[-1]} que es el ultimo') 

# 🔟 BONUS 🔥 mini sistema con lista
# numeros = [12, 7, 25]

# Crea un programa que diga:
# cuál es el mayor de los 3
# cuál es el menor
# cuántos son pares

# 👉 todo usando índices e if

numeros = [12, 7, 25]

numero1 = numeros[0]
numero2 = numeros[1]
numero3 = numeros[2]
mayor = numero1

if mayor < numero2: 
    mayor = numero2
if mayor < numero3:
    mayor = numero3

print('El numero mayor es:', mayor)

menor = numero1

if menor > numero2:
    menor = numero2
if menor > numero3:
    menor = numero3
print('El numero menor es:', menor)

if numeros[0] % 2 == 0  and numeros[1] % 2 == 0 and numeros [2] % 2 == 0:
    print('Hay 3 numeros pares')
elif numeros[0] % 2 == 0  and numeros[1] % 2 == 0 and numeros [2] % 2 == 1:
    print('Hay 2 numeros pares')
elif numeros[0] % 2 == 0  and numeros[1] % 2 == 1 and numeros [2] % 2 == 0:
    print('Hay 2 numeros pares')
elif numeros[0] % 2 == 1  and numeros[1] % 2 == 0 and numeros [2] % 2 == 0:
    print('Hay 2 numeros pares')
elif numeros[0] % 2 == 0  and numeros[1] % 2 == 1 and numeros [2] % 2 == 1:
    print('Hay 1 numero par')
elif numeros[0] % 2 == 1  and numeros[1] % 2 == 0 and numeros [2] % 2 == 1:
    print('Hay 1 numero par')
elif numeros[0] % 2 == 1  and numeros[1] % 2 == 1 and numeros [2] % 2 == 0:
    print('Hay 1 numero par')
else:
    print('no hay pares')


### solución GPT

numeros = [12, 7, 25]

contador_pares = 0

if numeros[0] % 2 == 0:
    contador_pares += 1

if numeros[1] % 2 == 0:
    contador_pares += 1

if numeros[2] % 2 == 0:
    
    contador_pares += 1

print("Hay", contador_pares, "numeros pares")