print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

print("Camilo \n" + "Bogotá")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))        # int
print(type(b))        # float 
print(type(c))        # str
print(type(d))        # bool
print(type(e))        # NoneType

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print(int("12345"))  # convierte el string "12345" a int = 12345
print(float("12345"))# convierte el string "12345" a float = 12345.0
print(int(3.99))     # convierte el float 3.99 a int = 3 (trunca los decimales)

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nombre = "camilo"
edad = 31
altura = 1.75

print(f"Hola! Mi nombre es {nombre}, Tengo {edad} años y mido {altura} metros")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.14159
rounded_pi = round(pi)
int_division = rounded_pi // 2
print(int_division)
