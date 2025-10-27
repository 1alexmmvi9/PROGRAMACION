'''
    Aplicaciones de gestión de productos
    (c) 2025 Alex Sytnyk
    Esta aplicación gestiona productos
'''

# En esta aplicacion no aplica importar librerias 

# Definimos clases y funciones

class Producto():
    def __init__(self):
        self.nombre = ""
        self.precio = 0 

# Creamos las variables globales

productos = []

# Primer olanzamos un mensaje de bienvenida
print("Gestor de productos v0.1 Alex Sytnyk")
# Metemos al usuario a un bucle infinito controlado
while True:
    # Le mostramos al usuario las opciones que tiene
    print("Selecciona una opcion: ")
    print("1. -Crear un nuevo producto")
    print("2. -Listar los productos")
    print("3. -Actualizar lso productos")
    print("4. -Eliminar los producto")
    opcion = int(input("Escoge una opcion: "))
    # En funcion de la opcion que coja el usuario
    if opcion == 1:
        # O bien creamos un nuevo producto
        print("Creamos un nuevo producto")
    elif opcion == 2:
        # O bien listamos los productos
        print("Vamos a listar los productos")
    elif opcion == 3:
        # O bien actualizamos los productos
        print("Vamos a actualizar los productos")
    elif opcion == 4:
        # O bien eliminamos los productos
        print("Vamos a eliminar los productos")
    # Y volvemos a repetir