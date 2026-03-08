import os
os.system('cls')

# 🔥 Ahora el ejercicio completo

# Este ya mezcla varias cosas que has estado practicando.

# Usa este mismo diccionario:

# tienda = {
#     "frutas": {"manzana": 3000, "pera": 2500, "banana": 1800},
#     "verduras": {"zanahoria": 2000, "tomate": 2800, "cebolla": 1500},
#     "lacteos": {"leche": 3500, "queso": 5000}
# }
# Problema

# Crea un menú que permita al usuario hacer lo siguiente:

# 1. Ver todas las categorias
# 2. Ver productos de una categoria
# 3. Buscar precio de un producto
# 4. Salir

###
# Extra de GPT
###

# 🔥 Siguiente ejercicio (sube un poco el nivel)

# Vamos a expandir tu tienda.

# Agrega una nueva opción al menú:

# 5. Agregar producto

# Debe funcionar así:

# Ingrese categoria: frutas
# Ingrese nombre del producto: mango
# Ingrese precio: 3200

# Resultado:

# El producto se agrega al diccionario.

# Después si haces opción 2, debería aparecer:

# manzana - 3000
# pera - 2500
# banana - 1800
# mango - 3200

# 💡 Pistas:

# Necesitarás algo así:

# tienda[categoria][producto] = precio


tienda = {
    "frutas": {"manzana": 3000, "pera": 2500, "banana": 1800},
    "verduras": {"zanahoria": 2000, "tomate": 2800, "cebolla": 1500},
    "lacteos": {"leche": 3500, "queso": 5000, 'kefir': 4300}
}

print('-----------------------------------------')
print('-- Bienvenidos a la tienda de Camiilo --')
print('-----------------------------------------')

while True:
    print('\nEscriba el numero de la siguiente lista de posibilidades')
    print('''
1. Ver todas las categorias
2. Ver productos de una categoria
3. Buscar precio de un producto
4. Salir
''')
    
    try:
        user = int(input('Escriba la opción que desee: '))
        if user == 4:
            print('\nGracias por visitar la tienda de Camiilo')
            print('---------- Hasta la próxima! ----------')
            print('-----------------------------------------')
            break
        elif user == 1:
            print('\nLas categorias existentes son: \n')
            for categorias in tienda.keys():
                print(categorias)
        elif user == 2:
            user_categoria = input('\nIngrese la categoria de la que quiere saber los productos: ')
            print(f'\nIngresaste categoria → {user_categoria}\n')
            if tienda.get(user_categoria):
                for buscar_categoria, precio in tienda[user_categoria].items():
                    print(f'{buscar_categoria} : {precio}')
            else: 
                print(tienda.get(user_categoria, 'Categoria no encontrada!'))
        elif user == 3:
            user_producto = input('\nEscriba el producto del que quiere saber el precio: ')
            print(f'\nIngresaste producto → {user_producto}\n')
            encontrado = False
            for buscar_pruducto in tienda.values():
                if buscar_pruducto.get(user_producto):
                    print(f'El producto tiene un precio de: {buscar_pruducto[user_producto]}')
                    encontrado = True
                    break
            if not encontrado:
                print('Producto no encontrado')
    except ValueError:
        print('\nEl valor ingresado no es un número!!')
        print('Vuelve a intestarlo \n')