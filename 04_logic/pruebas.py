import os
os.system('cls')

# 9️⃣ Conteo de pares usando diccionario

# Dada una lista de números:
# Crea un diccionario con:

# "pares": cantidad
# "impares": cantidad

# Usando tu función par().

def par(a):
    return a % 2 == 0

list_number = [39, 58, 56, 68, 28, 49, 66, 52, 12, 7, 45, 45, 48, 23, 52, 31, 45, 46, 63, 15]
list_par = []
list_impar = []
dict_number = {}
dict_par = {}
dict_impar = {}

for number in list_number:
    if par(number):
        list_par.append(number)
        
    else:
        list_impar.append(number)

total_par = len(list_par)
total_impar = len(list_impar)

dict_par['lista_pares'] = list_par
dict_par['total_pares'] = total_par
dict_impar['lista_impares'] = list_impar
dict_impar['total_impares'] = total_impar

dict_number['pares'] = dict_par
dict_number['impares'] = dict_impar
print(dict_number)