import os
os.system('cls')

# 🔴 🧩 NIVEL DIFÍCIL (estructura mental)

# 7️⃣ Diccionario de listas

# Crea un diccionario donde:

# Cada clave sea un nombre de estudiante.
# Cada valor sea una lista de 3 notas.

# Luego:

# Calcula el promedio de cada estudiante.
# Determina cuál tiene el promedio más alto.

print('!Bienvenido!')
print('Portal de profesores')

dic_estudiantes = {}
dic_promedios = {}

def promedio(a):
    promedio = 0
    for n in a:
        promedio += n
    return promedio / 3

while True:
    contador = 0
    notas = []
    print('Desea agregar un estudiante?')
    continuar = input('Escriba si/salir: ').lower()
    if continuar == 'salir':
        print('Gracias, nos vemos en la proxima!')
        break
    estudiante = input('Escribe el nombre del estudiante: \n')
    while contador < 3:
        nota = float(input('Agregue las notas del estudiante: '))
        notas.append(nota)
        contador += 1
    dic_estudiantes[estudiante] = notas
    dic_promedios[estudiante] = promedio(notas)


print('Los promedios de los estudiantes son: ', dic_promedios)

for nombre, max_promedio in dic_promedios.items():
    if max_promedio == max(dic_promedios.values()):
        print(f'El estudiante con mayor promedio es {nombre} y es de {max_promedio}')
