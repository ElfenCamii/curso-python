###
# 05 - entrada de usuario (input?()) - version simplificada
# la funcion input() nos permite pedir datos al usuario atraves de la consola
# la funcion input() siempre devuelve un string
###

nombre = input("cual es tu nombre? \n")  # el texto entre comillas se muestra como mensaje al usuario
print(f"hola {nombre}, bienvenido a python")  # f-string permite insertar variables dentro de una cadena

age = input("cuantos años tienes? \n")  # input() devuelve un string
age = int(age)  # convertimos el string a entero    
print(f"dentro de 10 años tedras {age + 10} años")  # sumamos 10 al entero

print("Obtener multiples valores a la vez")
country, city = input("En que pais y ciudad vives? \n").split()
print(f"vives en {city}, {country}")
# la funcion split() divide el string en una lista de strings, usando el espacio como separador
# si el usuario ingresa "Argentina Buenos Aires", country sera "Argentina" y city sera "Buenos Aires"
