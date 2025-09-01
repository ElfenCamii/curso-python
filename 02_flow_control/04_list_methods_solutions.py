# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

import os
os.system("cls")

print('\nEjercocop 1: Añadir y modificar elementos')
lista_numeros = [1, 2, 3, 4, 5]
print(f'Lista original \n{lista_numeros}')
lista_numeros.append(6)
print(f'Agregar el numero 6 al final de la lista \n{lista_numeros}')
lista_numeros.insert(2, 10)
print(f'Agregando el numero 10 en la segunda posición de la listra \n{lista_numeros}')
lista_numeros[0] = 0
print(f'Reemplazando el valor inicial de la lista por un 0 \n{lista_numeros}')


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

print('\nEjercicio 2: Combinar y limpiar listas')
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
print(f'Listas originales: ')
print(f'Lista a {lista_a} \nLista b {lista_b}')
lista_a.extend(lista_b)
print(f'Extendiendo la lista b a la lista a \n{lista_a}')
lista_a.remove(1)
print(f'Eliminando la primera aparición del numero 1 en la lista a \n{lista_a}')
elemento_3 = lista_a.pop(3)
print(f'El elemenrto eliminado en el indice 3 de la lista es el "{elemento_3}"')
print(f'La lista sin dicho elemento es \n{lista_a}')
lista_b.clear()
print(f'La lista b luego de usar .clear es la siguiente \n{lista_b}')


# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

print('\nEjercicio 3: Slicing y eliminación con "del"')
lista_del = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'La lista original es: \n{lista_del}')
del lista_del[2:5]
print(f'La lista con los elementos eliminados del 2 al 5 sin incluir el 5 es la siguiente:')
print(lista_del)


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

print('\nEjercicios 4: Ordenar y contar')
lista_ordenada = [5, 2, 8, 1, 9, 4, 2]
print(f'La lista original es la siguiente {lista_ordenada}')
lista_ordenada.sort()
print(f'La lista ordenada es la siguiente {lista_ordenada}')
print(f'La cantidad de veces que hay un 2 en la lista es "{lista_ordenada.count(2)}"')
print(f'Hay un numero 7 en la lista "{'7' in lista_ordenada}"')


# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

print('\nEjercicio 5: Copia vs Referencia')
original = [1, 2, 3]
copia_1 = original[:]
copia_2 = original.copy()
referencia = original[:]
referencia[0] = 10
print(f'la lista original es:')
print(original)
print('La lista copia 1 es:')
print(copia_1)
print('La lista copia 2 es:')
print(copia_2)
print('La lista referencia es:')
print(referencia)


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

print('\nEjercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas')
mercado = ["Manzana", "pera", "BANANA", "naranja"]
mercado.sort(key=str.lower)
print(f'La lista del mercado ordenada sin importar las mayúsculas y minúsculas: \n{mercado}')