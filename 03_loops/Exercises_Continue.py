# 🟡 Ejercicio 2 — Simulación tipo entrevista
# 🎯 Objetivo:

# Pedir números al usuario.
# Si escribe algo que no sea número, ignorarlo.
# Si escribe número negativo, ignorarlo.
# Solo imprimir los positivos válidos.
# Salir cuando escriba 0.

# Estructura mental correcta:

# Si es 0 → break
# Si no es número → continue
# Si es negativo → continue
# Si pasa todo → imprimir
import os
os.system('cls')

while True:
    entrada = input("Escribe un numero (0 para salir): ")

    try:
        numero = int(entrada)
    except ValueError:
        print("No es un numero valido")
        continue

    if numero == 0:
        break

    if numero < 0:
        print("Numero negativo ignorado")
        continue

    print("Numero valido:", numero)

# 🎯 Ahora sí te pongo uno que SÍ debes completar tú

# Nuevo ejercicio:

# Pedir números.
# Ignorar los múltiplos de 5.
# Salir cuando escriban 0.
# Imprimir solo los números válidos.

while True:
    entrada = input('Escribe un numero (0 para salir)')

    try:
        numero = int(entrada)
    except ValueError:
        print('No es un numero')
        continue
    if numero == 0:
        print('Gracias, hasta la proxima')
        break
    if numero % 5 == 0:
        continue
    print('numero valido', numero)

    # Aquí debes poner:
    # 1. Salir si es 0
    # 2. Ignorar si es multiplo de 5
    # 3. Imprimir si es valido