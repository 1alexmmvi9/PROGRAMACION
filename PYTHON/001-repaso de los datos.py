class Gato():
    def __init__(self):
        self.color = ""     # Esto es una propiedad
    
    def maulla(self):
        return "miau"
    
    def setColor(self,nuevocolor):      # Defino un setter - el método es el responsable de cambiar la propiedad
        self.color = nuevocolor

    gato1 = Gato()
    gato1.color = "naranja"

    gato1.setColor("naranja")

    print(gato1.color)

    print(gato1.getColor())