###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion
###

print('\nBucle while')

# Bucle con una simple condición
contador = 0
while contador <= 5:
    print(contador)
    contador += 1   #La condición es super importante para evitar un bucle infinito


print('\nBucle while con break')
# Utilizando la palabra brak, para romper un bucle

contador = 0
while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle

# Ejemplo de bucle con break
print('\nContador decreciente de 100 que encuentra el primer multipo de 5')
contador = 100
while contador >= 0:
    contador -= 1
    print(contador)
    if contador % 5 == 0:
        print(f'El numero {contador} es multiplo de 5')
        break   #sale del bucle


# Continue, lo que hace es saltar esa interacción en concreto
# y continuar con el bucle
print('\nBucle con continue')
contador = 0
while contador < 10:
   contador += 1
   if contador % 2 == 0:
      continue
   print(contador)


# else, esta condición cuando se ejecuta?
print('\nBucle while con else:')
contador = 0
while contador < 5:
   print(contador)
   contador += 1
else:
   print('El bucle a terminado')


###
# Pedirle al usuario un número que tiene
# que ser positivo si no, no dejamos de pregutnar
###

# Modo simple
numero = -1 # Para tener un punto de partida
while numero <= 0:
   numero = int(input("Escribe un número positivo: "))
   if numero <= 0:
      print(f'El numero es {numero} y no es un numero positivo, intentalo nuevamente')

print(f'El número que has introducido es {numero}, el cual si es un número positivo, bien hecho!!!')

# Modo a prueba de fallos con TRY
numero = -1 # Para tener un punto de partida
while numero <= 0:
    try:
      numero = int(input("Escribe un número positivo: "))
      if numero <= 0:
        print(f'El numero es {numero} y no es un numero positivo, intentalo nuevamente')
    except:
      print("Lo que introduces debe de ser un número, que si no no funciona")

print(f'El número que has introducido es {numero}, el cual si es un número positivo, bien hecho!!!')