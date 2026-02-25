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
    print(contador)
    if contador % 2 == 0:
        pares += 1
        print(contador)
    contador += 1
print(pares)