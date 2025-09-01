###
# 04 - Listas Métodos
# Los métodos más importantes para trabajar con listas
###

import os
os.system("cls")

lista1 = ['a', 'b', 'c', 'd']
print(lista1)

lista1.append('e')    # Añade un elemento al final de la lista
print(lista1)

lista1.insert(1, '@')   # Inserta un elemento en la posicion que le indiquemos como argumento
print(lista1)

lista1.extend(['y', 'z'])   # Agrega elementos al final de la lista
print(lista1)

lista1.remove('@')  # Elimina la primera aparicion de un elemento
print(lista1)

ultimo = lista1.pop()   # Elimina el ultimo elemento de la lista y ademas te lo devuelve
print(ultimo)
print(lista1)

lista1.pop(1)   # Elimina el segundo elemento de la lista (es el indice 1)
print(lista1)

del lista1[-1]  # Elimina a lo bestia
print(lista1)

lista1.clear()  # Elimina todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['🍕', '🍔', '🍟', '🌭', '🍿']
print(lista1)
del lista1[1:3]
print(lista1)

# Más métodos útiles
print('Ordenar listas modioficando la original')
numbers = [3, 10, 2, 8, 99 ,193]
numbers.sort()
print(numbers)

print('Ordenar listas creando una copia de la original')
numbers = [3, 10, 2, 8, 99 ,193]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print("\nOrdenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("\nOrdenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print(len(animals)) # Tamaño de la lista -> 4
print(animals.count('🐶'))  # Cuenta cuantas veces aparece el elemento '🐶' -> 2
print('🐼' in animals)  # Comprueba si hay un '🐼' en la lista -> True
print('🐹' in animals)  # -> False