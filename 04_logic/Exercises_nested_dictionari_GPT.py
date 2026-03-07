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
list_categoria = []
list_productos = []
list_precios = []

def productos(a):
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
            for b_categoria, b_productos in tienda.items():
                print(b_productos.get(busqueda_p, 'El producto buscado no se encuentra en existencia!'))
        elif user == 4:
            print('gracas por visitarnos\nHasta la proxima')
            break
        else:
            print('Valor asignado no valido')
    except ValueError:
        print('El valor ingresado no es un numero')