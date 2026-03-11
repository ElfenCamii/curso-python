import os
os.system('cls')

# 8️⃣ Diccionario anidado

# Crea un sistema tipo agenda:

# agenda = {
#     "Camilo": {"telefono": "123", "ciudad": "Bogotá"},
#     "Ana": {"telefono": "456", "ciudad": "Medellín"}
# }

# Permite buscar una persona y mostrar sus datos.
# Maneja el caso donde no exista.

agenda = {
    "Camilo": {"telefono": "123", "ciudad": "Bogotá"},
    "Ana": {"telefono": "456", "ciudad": "Yopal"},
    "Daniella": {"telefono": "890", "ciudad": "Medellín"}
}

print('----------------------------------------')
print('--- Bienvenidos a tu agenda personal ---')
print('----------------------------------------')

while True:
    print('''
\nEscribe el número de la opción que desees:
          
    1. Buscar a una persona
    2. Salir
''')
    
    try:
        user = int(input('Que deseas hacer: '))
        if user == 2:
            print('--------------------------')
            print('-------- Gracias! --------')
            print('--- Hasta la proxima!! ---')
            print('--------------------------')
            break
        elif user == 1:
            user_persona = input('\nIngrese el nombre de la persona que desea buscar: ').capitalize()
            print(f'\nIngresaste el nombre de → {user_persona}')
            if agenda.get(user_persona):
                for name in agenda[user_persona].keys():
                    print(f'{name} : {agenda[user_persona]}')
            else:
                print(agenda.get(user_persona, 'La persona buscada no se encuentra en la agenda'))
    except ValueError:
        print('\nEl valor ingresado no es un número')
        print('Intente nuevamente, gracias!')