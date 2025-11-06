# Un programa que puede permanecer los datos de los clientes que se inserte
#v0.1 Alex Sytnyk

import pickle

class Cliente:
    def __init__(self, nombre, apellidos, gmail):
        self.nombre = nombre
        self.apellidos = apellidos
        self.gmail = gmail

# Intentamos abrir la lista de clientes guardada con pickle
try:
    with open("clientes.pkl", "rb") as archivo:
        clientes = pickle.load(archivo)
        print("Lista de clientes cargada correctamente.\n")
except:
    clientes = []
    print("No se encontró ninguna lista guardada, se creará una nueva.\n")

# Este es el bucle principal del menú
while True:
    print("\n--- MENÚ DE CLIENTES ---")
    print("1. Crear cliente")
    print("2. Listar clientes")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        gmail = input("Gmail: ")

        nuevo_cliente = Cliente(nombre, apellidos, gmail)
        clientes.append(nuevo_cliente)

        with open("clientes.pkl", "wb") as archivo:
            pickle.dump(clientes, archivo)

        print("\nCliente guardado correctamente.")

    elif opcion == "2": # Desde esta linea (43) hasta la línea (55) lo he copiado tal cual de un ejercicio que hice en casa de repaso
        print("\n--- LISTA DE CLIENTES ---")
        if len(clientes) == 0:
            print("No hay clientes registrados.")
        else:
            for x, y in enumerate(clientes, start=1):
                print(f"{x}. {y.nombre} {y.apellidos} - {y.gmail}") # Esto me lo ha ayudado chat gpt porque no sabia bien como poner: (f"{}...)

    elif opcion == "3":
        print("Saliendo de la aplicación...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")