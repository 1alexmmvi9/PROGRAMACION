class Cliente():
    def __init__(self):
        self.nombrecompleto = ""
        self.emeil = ""
    def setNombreCompleto(self,nuevonombre):
        self.nombrecompleto = nuevonombre
    def setEmail(self,nuevoemail):
        self.email = nuevoemail
    def getNombreCompleto(self):
        return self.nombrecompleto
    def getEmail(self):
        return self.email
    
clientes = []
    
    # CRUD

print("Gestor de clientes v0.1 Alex Sytnyk")

while True:
    print("Selecciona una opción")
    print("1. -Insertar un nuevo cliente")
    print("2. -Obtener listado de clientes")
    opcion = int(input("Indica tu opción (1,2): "))

    if opcion == 1:
        print("Voy a insertar un cliente")
        nuevocliente = Cliente()
        nombrecliente = input("Introduce el nombre del cliente: ")
        nuevocliente.setNombreCompleto(nombrecliente)
        emailcliente = input("Introduce el email del cliente: ")
        nuevocliente.setEmail(emailcliente)
        clientes.append(nuevocliente)
    elif opcion == 2:
        print("Saco el listado de clientes")
        for cliente in clientes:
            print("----------------------")
            print("nombre: ",cliente.getNombreCompleto())
            print("email: ",cliente.getEmail())
            print("----------------------")
