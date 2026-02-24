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
