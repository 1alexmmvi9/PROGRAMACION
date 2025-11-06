# Programa de creacion de clases
# v0.1 Alex Sytnyk
# Pide la informacion a los clientes

class Cliente:
    def __init__(self, nombre, apellidos, gmail):
        self.nombre = nombre
        self.apellidos = apellidos
        self.gmail = gmail

    def set_gmail(self, nuevo_gmail):
        self.gmail = nuevo_gmail

    def get_gmail(self):
        return self.gmail


# Creacion de 3 instancias de la clase (pueden ser mas o menos, son 3 justo para este ejercicio)
cliente1 = Cliente("Alex", "Sytnyk", "alex.sytnyk@gmail.com")
cliente2 = Cliente("JoseVicente", "Carratala", "josevicente.carratala@gmail.com")
cliente3 = Cliente("Andres", "Ruiz", "andres.ruiz@gmail.com")

# Mostrar los gmails de cada cliente usando get_gmail()
print("Gmail cliente 1:", cliente1.get_gmail())
print("Gmail cliente 2:", cliente2.get_gmail())
print("Gmail cliente 3:", cliente3.get_gmail())

# Cambiar los gmails usando set_gmail()
cliente1.set_gmail("nuevo.gmail.alex@gmail.com")
cliente2.set_gmail("nuevo.gmail.josevicente@gmail.com")
cliente3.set_gmail("nuevo.gmail.andres@gmail.com")

# Comprobar que los métodos set y get funcionan correctamente
print("\nGmails actualizados:")
print("Gmail cliente 1:", cliente1.get_gmail())
print("Gmail cliente 2:", cliente2.get_gmail())
print("Gmail cliente 3:", cliente3.get_gmail())
