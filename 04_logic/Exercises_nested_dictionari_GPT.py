import os
os.system('cls')

# 1 ejercicio de diccionarios que tenga diccionarios anidados

# Algo tipo:

# tienda = {
#     "frutas": {"manzana": 3000, "pera": 2500},
#     "verduras": {"zanahoria": 2000, "tomate": 2800}
# }

# Y el ejercicio podría ser:

# mostrar todos los productos
# mostrar precios
# buscar un producto

tienda = {
    "frutas": {"manzana": 3000, "pera": 2500},
    "verduras": {"zanahoria": 2000, "tomate": 2800}
}


def productos(a):
    '''
    Función que permite mostrar las categorias, los productos y los precios de la tienda de Camiilo
    '''
    list_categoria = []
    list_productos = []
    list_precios = []

    for categoria, stok in a.items():
        list_categoria.append(categoria)
        for producto, precio in stok.items():
            list_productos.append(producto)
            list_precios.append(precio)
    return list_categoria, list_productos, list_precios

categoria, producto, precios = productos(tienda)

print('Bienvenidos a la tienda de Camiilo')

while True:
    print('\nEscriba el numero de la acción que desee: ')
    print('''
1: Para ver los productos
2: Para buscar una categoria
3: Para buscar un producto
4: para salir del programa 
''')
    
    try:
        user = int(input('Que decea hacer: '))
        if user == 1:
            print('La tienda cuenta con las siguentes categorias:\n', categoria)
            print('En las que cuenta con los siguientes productos:\n', producto)
            print('Acontinuacion se muestra respectivamente los precios de esos productos:\n', precios)
        elif user == 2:
            busqueda_c = input('Ingrse la categoria que quiera buscar: ')
            print(tienda.get(busqueda_c, 'La categoria buscado no se encuentra en existencia!'))
        elif user == 3:
            busqueda_p = input('Ingrse el producto que quiera buscar: ')
            encontrado = False
            for b_categoria, b_productos in tienda.items():
                if busqueda_p in b_productos:
                    print(f'el precio de {busqueda_p} es de {b_productos[busqueda_p]}')
                    encontrado = True
            if not encontrado:
                print('El producto buscado no se encuentra en existencia')
        elif user == 4:
            print('gracas por visitarnos\nHasta la proxima')
            break
        else:
            print('Valor asignado no valido')
    except ValueError:
        print('El valor ingresado no es un numero')


###
# Extra para lectura de diccionarios anidados
###

# Ejercicio rápido

# Con el mismo diccionario tienda imprime:

# Categoria: frutas
# - manzana: 3000
# - pera: 2500

# Categoria: verduras
# - zanahoria: 2000
# - tomate: 2800

# Usando dos for anidados.

for extra_categorias, extra_productos in tienda.items():
    print(f'\nCategoria: {extra_categorias}')
    for extra_producto, extra_precio in extra_productos.items():
        print(f'- {extra_producto}: {extra_precio}')

# Para cerrar el día te dejo un mini-reto de 3 minutos (muy corto)

# Usando este diccionario:

# tienda = {
#     "frutas": {"manzana": 3000, "pera": 2500},
#     "verduras": {"zanahoria": 2000, "tomate": 2800}
# }

# Haz un programa que imprima solo los productos que valgan más de 2600.

# Salida esperada:

# manzana - 3000
# tomate - 2800

print('\nProductos con un precio superior a $2600')
for extra_productos in tienda.values():
    for extra_producto, extra_precio in extra_productos.items():
        if extra_precio > 2600:
            print(f'- {extra_producto}: {extra_precio}')

# Te dejo un último mini-reto opcional (nivel 3 minutos)

# Modificar tu código para que imprima también la categoría del producto.

# Salida esperada:

# frutas - manzana: 3000
# verduras - tomate: 2800

print('\nProductos con un precio superior a $2600 junto con su categoria:')
for extra_categorias, extra_productos in tienda.items():
    for extra_producto, extra_precio in extra_productos.items():
        if extra_precio > 2600:
            print(f'→ {extra_categorias} - {extra_producto}: {extra_precio}')