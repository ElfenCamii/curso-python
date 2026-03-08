import os
os.system('cls')

# 🔹 Ejercicio corto (5-10 minutos)

# Usa este diccionario:

# tienda = {
#     "frutas": {"manzana": 3000, "pera": 2500, "banana": 1800},
#     "verduras": {"zanahoria": 2000, "tomate": 2800, "cebolla": 1500},
#     "lacteos": {"leche": 3500, "queso": 5000}
# }
# Problema

# Imprime cuántos productos hay en cada categoría.

# Salida esperada:

# frutas tiene 3 productos
# verduras tiene 3 productos
# lacteos tiene 2 productos

# 💡 Pista:
# Necesitarás usar len().

tienda = {
    "frutas": {"manzana": 3000, "pera": 2500, "banana": 1800},
    "verduras": {"zanahoria": 2000, "tomate": 2800, "cebolla": 1500},
    "lacteos": {"leche": 3500, "queso": 5000}
}

for categorias, productos in tienda.items():
    n_productos = len(productos)
    print(f'{categorias} tiene {n_productos} productos')