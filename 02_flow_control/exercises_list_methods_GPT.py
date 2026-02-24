import os
os.system('cls')

# 🧠 1️⃣ Agregar elementos dinámicamente

# Crea una lista vacía.
# Pide al usuario 3 números y agrégalos a la lista usando append().
# Imprime la lista final.

user_number1 = int(input('Ingrese el primer numero que dese para la lista: '))
user_number2 = int(input('Ingrese el segundo numero que dese para la lista: '))
user_number3 = int(input('Ingrese el tercer numero que dese para la lista: '))

number_list = []
number_list.append(user_number1)
number_list.append(user_number2)
number_list.append(user_number3)
print(number_list)

# 🧠 2️⃣ Insertar en posición específica
# numeros = [10, 20, 40, 50]

# Inserta el número 30 en la posición correcta para que quede ordenada.
# Usa insert().

numbers = [10, 20, 40, 50]
numbers.insert(2, 30)

print(numbers)

# 🧠 3️⃣ Eliminar un elemento por valor
# frutas = ["manzana", "pera", "uva", "pera"]

# Elimina solo una "pera" usando remove().
# Imprime la lista.

frutas = ["manzana", "pera", "uva", "pera"]
frutas.remove('pera')

print(frutas)

# 🧠 4️⃣ Eliminar por posición
# colores = ["rojo", "azul", "verde", "amarillo"]

# Elimina el último elemento usando pop().

# Imprime:
# el elemento eliminado
# la lista actualizada

colors = ["rojo", "azul", "verde", "amarillo"]
color = colors.pop()

print("Elemento eliminado:", color)
print("Lista actualizada:", colors)

# 🧠 5️⃣ Buscar posición de un elemento
# nombres = ["ana", "luis", "camilo", "maria"]

# Pide un nombre al usuario y muestra su posición usando index().
# (Si no está, muestra mensaje adecuado con if antes de usar index()).

user_name = input('Ingrese el nombre que desea saber: ').lower()
names = ["ana", "luis", "camilo", "maria"]

if user_name in names:
    print(f'El nombre esta en la posición {names.index(user_name)}')
else:
    print('El nombre no esta en la lista')
