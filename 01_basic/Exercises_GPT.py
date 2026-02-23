# 1️⃣ Imprimir texto con saltos de línea

# Escribe un programa que imprima:

# Hola
# Soy Camilo
# Estoy aprendiendo Python

print('Hola')
print('Soy Camiilo')
print('Estoy aprendiendo Python')


# 2️⃣ Operaciones básicas

# Crea dos variables:

# a = 10
# b = 3

# Imprime:
# suma
# resta
# multiplicación
# división normal
# división entera
# residuo (módulo)

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

# 3️⃣ Conversión de tipos

# Convierte:

# el número 25 a string
# el string "45.67" a float
# el float 10.99 a entero
# Imprime cada resultado

numero = 25
print(f'El tipo original era {type(numero)}, el valor era {numero} y el nuevo tipo es:{type(str(numero))}')
texto = '45.76'
print(f'El tipo original era {type(texto)}, el valor era {texto} y el nuevo tipo es: {type(float(texto))}')
entero = 10.99
print(f'El tipo original era {type(entero)}, el valor era {entero} y el nuevo tipo es: {type(int(entero))}')

# 4️⃣ Entrada de datos del usuario

# Pide al usuario:
# su nombre
# su edad
# e imprime:
# Hola Camilo, el próximo año tendrás 26 años

name = input('Dime cual es tu nombre: ')
age = int(input('Dime cual es tu edad: '))

print(f'Hola {name}, el próximo año tendrás {age + 1} años')

# 5️⃣ Uso de len()

# Crea una variable con tu nombre completo

# Imprime:

# la longitud del texto
# el primer carácter
# el último carácter

full_name = 'Camilo Andres Pinto Angulo'

print(f'La longitud del texto es de: {len(full_name)} caracteres')
print(f'Primer carácter: {full_name[0]}')
print(f'El ultimo caracter es: {full_name[-1]}')

# 6️⃣ Strings: mayúsculas y minúsculas

# Dado el texto:
# texto = "python es genial"
# Imprime:
# todo en mayúsculas
# todo en minúsculas
# la primera letra en mayúscula

text = 'Python es genial'

print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title()) # Primera letra de cada palabra en mayuscula

# 7️⃣ Reemplazo de texto

# Dado:
# frase = "Me gusta Java"
# Reemplaza la palabra Java por Python

frase = 'Me gusta Java'
new_frase = frase.replace('Java', 'Python')

print(new_frase)