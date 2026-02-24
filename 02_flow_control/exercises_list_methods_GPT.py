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

# 🧠 6️⃣ Contar repeticiones
# numeros = [1, 2, 3, 2, 4, 2, 5]

# Cuenta cuántas veces aparece el número 2 usando count().

numeros = [1, 2, 3, 2, 4, 2, 5]
repetido = numeros.count(2)

print('El numero de veces que se repite el numero 2 es: ', repetido, 'veces')

# 🧠 7️⃣ Ordenar lista
# numeros = [8, 3, 12, 1, 7]

# Ordénala de menor a mayor usando sort().
# Luego imprímela.

lista_numeros = [8, 3, 12, 1, 7]
lista_ordeenada = sorted(lista_numeros)

print('La lista original es: ', lista_numeros)
print('La lista ordeenada es:', lista_ordeenada)

lista_numeros.sort()
print('La lista original ordenada: ', lista_numeros)

# 🧠 8️⃣ Ordenar al revés

# Usa la misma lista anterior.
# Ordénala de mayor a menor sin usar sorted().
# (Pista: sort() + algo más).

lista_numeros = [8, 3, 12, 1, 7]
lista_numeros.sort(reverse=True)

print('La lista original ordenada: ', lista_numeros)

# 🧠 9️⃣ Copiar lista
# original = [1, 2, 3]

# Crea una copia usando copy().
# Agrega un número a la copia.
# Imprime ambas listas y observa qué pasa.

original = [1, 2, 3]
copia = original.copy()
copia.append(4)

print('Lista original: ', original)
print('Copia de la lista original: ',copia)

# 🧠 🔟 BONUS – Mini sistema interactivo 🔥

# Crea un pequeño menú:
# Agregar número
# Eliminar número
# Mostrar lista
# Salir

# Usa:
# append()
# remove()
# pop()

# 👉 Mantén el programa simple (sin while si aún no lo has visto, puedes simularlo con varias ejecuciones).

list_numbers = [3, 5, 12, 53, 1, 0]
show_list = input('Quieres ver la lista? si/no: ').lower()

if show_list == 'si':
    print('La lista es: ', list_numbers)

add_number = input('Quieres agregar un numero? si/no: ').lower()

if add_number == 'si':
    number_user_add = int(input('Escriba el numero que quiere agregar: '))
    list_numbers.append(number_user_add)
    print('La nueva lista es: ', list_numbers)

delet_numbeer = input('Quieeres eliminar un numero de la lista? si/no: ').lower()

if delet_numbeer == 'si':
    number_user_delet = int(input('Escriba el numero que quieree eliminar: '))
    list_numbers.remove(number_user_delet)
    print('La nueva lista es: ', list_numbers)

pop_number = input('Quieres eliminar el ultimo numero de la lista? si/no: ')

if pop_number == 'si':
    list_numbers.pop()
    print('La nueva lista es: ', list_numbers)