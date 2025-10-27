# Las propiedades son como las variables PERO dentro de una clase

class Cliente():
    def __init__(self):
        self.nombre = ""
        self.nombre = 0
        self.telefonos = []

# Ahora instancio un nuevo objeto
cliente1 = Cliente()

# Ahora le escibo una propiedad

cliente1.nombre = "Alex Sytnyk"

print("El nombre del cliente es:",cliente1.nombre)

cliente1.telefonos.append("5467189")
cliente1.telefonos.append("5647820")

print(cliente1.telefonos)
